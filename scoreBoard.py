#!/usr/bin/env python3
# -*- utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from socket import *
from threading import Thread
from threading import Event
import time
import sys
import serial
import serial.tools.list_ports

DEFAULT_BAUDRATE = 115200
DEFAULT_BYTESIZE = 8
DEFAULT_STOPBIT = 1
DEFAULT_PARITY = 'N'

class App(Frame):
	def __init__(self):
		self.ser_addr = ('192.168.4.3', 8086)
		self.nums_online = 0                  # 上线人数
		self.max_con_num = 8                  # 最大连接数
		self.port_list = {}
		self.ser = serial.Serial()
		self.recv_thread = None     #　线程

		self.back_ground = 'DimGray'          # 背景颜色
		Frame.__init__(self, bg=self.back_ground)
		self.pack(expand=YES, fill=BOTH)
		self.master.geometry('+200+200')
		self.master.minsize(width=800, height=300)
		self.master.title('ScoreBoard')
		self.text = StringVar()
		self.build_gui()
		self.thread_running = Event()


	# 主界面
	def build_gui(self):
		self.score_board = Label(self, text='ScoreBoard', bg=self.back_ground).pack(expand=YES, fill=BOTH)

		self.tree = ttk.Treeview(self, show="headings", columns=('ID', 'IP', 'Port', 'Score', 'Status'))
		self.tree.column('ID', width=50)
		self.tree.column('IP', width=100)
		self.tree.column('Port', width=50)
		self.tree.column('Score', width=50)
		self.tree.column('Status', width=50)
		self.tree.heading("ID", text="ID")
		self.tree.heading("IP", text="IP")
		self.tree.heading("Port", text="Port")
		self.tree.heading("Score", text="Score")
		self.tree.heading("Status", text="Status")   # on-line off-line
		for i in range(8):
			self.tree.insert('', i, values=(i+1, 'Unknown', 'Unknown', 0, 'Off-line'))
		self.tree.pack(under=self.score_board, expand=YES, fill=BOTH)

		self.text.set('无串口')
		self.status_bar = Label(self, 
			bg=self.back_ground,
			textvariable=self.text)
		self.status_bar.pack(after=self.tree, expand=YES, fill=BOTH)

		self.port_search_label = Label(self, text='串口监测:')
		self.port_search_label.pack(after=self.status_bar, side=LEFT, expand=YES, fill=BOTH)	
		self.search_button = Button(self, text='搜索串口', command=self.port_search)
		self.search_button.pack(after=self.status_bar, side=LEFT, expand=YES, fill=BOTH)
		self.port_selc_label = Label(self, text='串口选择')
		self.port_selc_label.pack(after=self.status_bar, side=LEFT, expand=YES, fill=BOTH)
		self.combo_box = ttk.Combobox(self)
		self.combo_box.pack(after=self.status_bar, side=RIGHT, expand=YES, fill=BOTH)
		self.open_button = Button(self, text='打开串口', command=self.open_port)
		self.open_button.pack(after=self.status_bar, side=RIGHT, expand=YES, fill=BOTH)
		self.close_button = Button(self, text='关闭串口', command=self.close_port)
		self.close_button.pack(after=self.status_bar, side=RIGHT, expand=YES, fill=BOTH)
		self.check_button = Button(self, text='检查上线', command=self.send_data)
		self.check_button.pack(after=self.status_bar, side=RIGHT, expand=YES, fill=BOTH)

	# 定时器线程
	def timer_thread(self):
		self.recv_thread = Thread(target=self.recv_data)
		self.recv_thread.setDaemon(True)
		self.recv_thread.start()

	# 停止定时器线程
	def timer_thread_stop(self):
		self.thread_running.clear()

	# 搜索串口
	def port_search(self):
		self.port_list = list(serial.tools.list_ports.comports())
		temp = []
		print(len(self.port_list))
		self.combo_box.delete(0, END)
		if(len(self.port_list) > 0):
			for port in self.port_list:
				print(port[0])
				temp.append(port[0])

			self.combo_box['values'] = temp
			self.combo_box.current(0)
		self.combo_box['values'] = temp
		
	# 打开串口
	def open_port(self):
		self.ser.port = self.combo_box.get()
		self.ser.baudrate = DEFAULT_BAUDRATE
		self.ser.bytesize = DEFAULT_BYTESIZE
		self.ser.stopbits = DEFAULT_STOPBIT
		self.ser.parity = DEFAULT_PARITY
		try:
			self.ser.open()
			self.text.set('已打开'+self.combo_box.get())
		except Exception as e:
			print(e)
			messagebox.showwarning("Port Error", "此串口不能被打开！")
			return None

	# 关闭串口
	def close_port(self):
		try:
			self.timer_thread_stop()
			self.ser.flushOutput()
			self.ser.flushInput()
			self.ser.close()
			self.text.set('串口已关闭')
		except Exception as e:
			print(e)

	# 发送数据
	def send_data(self):
		if self.recv_thread is None:
			print('open thread')
			self.timer_thread() 
		print('send')
		if self.ser.isOpen():
			self.thread_running.set()
			self.ser.write('check\r\n'.encode('utf-8'))

	# 接收数据
	def recv_data(self):
		print('recv data')
		while self.thread_running.isSet():
			time.sleep(0.1)
			try:
				num = self.ser.inWaiting()
			except:
				self.close_port()
				return None
			if num > 0:
				data = self.ser.read(num)
				num = len(data)
				# if('OK' in data.decode()):
					# self.text.set('已打开'+self.combo_box.get() + ' 串口通信成功')
				print(data)
				# print(data.decode())
			else:
				pass

if __name__ == '__main__':
	App().mainloop()
