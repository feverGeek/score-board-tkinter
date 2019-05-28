#!/usr/bin/env python3
# -*- coding : utf-8 -*-
import re
import sys
import serial
import serial.tools.list_ports
from ScoreBoardUi import Ui_Form
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel

class App(Ui_Form, QWidget):
	def __init__(self):
		self.ser = serial.Serial()
		# self.ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
		self.ip_pattern = re.compile(r'\r\n(.*?),.*')
		self.recvinfo_pattern = re.compile(r'IPD,.*?,.*?,(.*?),.*?:(.*)')

		self.client_info = {'ip_list' : [],
							'times' : []}
		self.max_con = 2

		super().__init__()
		self.setupUi(self)
		self.recv_timer = QTimer()  # 定时器接收数据
		self.recv_timer.timeout.connect(self.recv_data)
		self.init_connect()

	def init_connect(self):
		self.searchButton.clicked.connect(self.search_port)	
		self.openPortButton.clicked.connect(self.open_port)
		self.closePortButton.clicked.connect(self.close_port)
		self.sendConButton.clicked.connect(lambda: self.send_data('connect'))
		self.checkButton.clicked.connect(lambda: self.send_data('check'))

	def search_port(self):
		self.port_list = list(serial.tools.list_ports.comports()) 
		print(len(self.port_list))
		self.comboBox.clear()
		if(len(self.port_list) > 0):
			for port in self.port_list:
				self.comboBox.addItem(port[0])

	def open_port(self):
		DEFAULT_BAUDRATE = 115200
		DEFAULT_BYTESIZE = 8
		DEFAULT_STOPBIT = 1
		DEFAULT_PARITY = 'N'

		self.ser.port = self.comboBox.currentText()
		self.ser.baudrate = DEFAULT_BAUDRATE
		self.ser.bytesize = DEFAULT_BYTESIZE
		self.ser.stopbits = DEFAULT_STOPBIT
		self.ser.parity = DEFAULT_PARITY
		try:
			self.ser.open()
			self.label_2.setText(self.comboBox.currentText())
		except Exception as e:
			print(e)
			QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
			return None
		self.recv_timer.start(2)  # 打开定时器 2ms间隔

	def close_port(self):
		self.recv_timer.stop()
		try:
			self.ser.close()
			self.label_2.setText("串口已关闭")
		except Exception as e:
			print(e)

	def send_data(self, data):
		if self.ser.isOpen():
			self.ser.write((data+'\r\n').encode('utf-8'))

	def recv_data(self):
		try:
			num = self.ser.inWaiting()
		except:
			self.close_port()
			return None
		if num > 0:
			data = self.ser.read(num)
			num = len(data)
			self.parse_data(data)
		else:
			pass

	def parse_data(self, data):
		try:
			data = data.decode()
		except:
			pass	

		# 单片机发过来的所有已连接ip
		if self.ip_pattern.findall(data):
			print(self.ip_pattern.findall(data))
			self.client_info['ip_list'].append(self.ip_pattern.findall(data)[0])
			self.client_info['times'].append(0)
			print('<---ip_list---')
			if len(self.client_info['ip_list']) is self.max_con:
				for row in range(self.max_con):
					self.model.appendRow([
						QStandardItem('%s' % (str(row+1))),
						QStandardItem('%s' % (self.client_info['ip_list'][row])),
						QStandardItem('0'),
						QStandardItem('On-line'),
					])
				self.tableView.setModel(self.model)
			print('---ip_list--->')
		elif self.recvinfo_pattern.findall(data):
			# 单片机发送过来的抢答信息
			print('<----抢答信息-----')
			info = self.recvinfo_pattern.findall(data)
			print(info)
			print(info[0][0])
			print(info[0][1])
			index = self.client_info['ip_list'].index(info[0][0])
			self.client_info['times'][index] += 1
			# TODO: 根据index的值修改times
			item = QStandardItem(self.client_info['times'][index])	
			self.model.setItem(index+1, 2, item)
			self.tableView.setModel(self.model)
			print('----抢答信息----->')

	def test(self):
		item = QStandardItem('test')
		self.model.setItem(1, 0, item)
		self.tableView.setModel(self.model)


if __name__ == '__main__':
	widget = QApplication(sys.argv)
	app = App()
	app.show()
	sys.exit(widget.exec_())