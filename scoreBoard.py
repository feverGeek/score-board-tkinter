#!/usr/bin/env python3
# -*- utf-8 -*-
from tkinter import *
from tkinter import ttk
from socket import *
from threading import Thread


class App(Frame):
	def __init__(self):
		self.back_ground = 'DimGray'  # 背景颜色
		self.nums_online = 	0         #　上线人数
		# self.ser_addr = ('192.168.4.3', 8086)
		# self.local_addr = ('192.168.4.15', 9999)
		self.ser_addr = ('127.0.0.1', 8086)
		self.local_addr = ('127.0.0.1', 9999)

		Frame.__init__(self, bg=self.back_ground)
		self.pack(expand=YES, fill=BOTH)
		self.master.geometry('+200+200')
		self.master.minsize(width=800, height=300)
		# self.master.geometry('400x300')
		self.master.title('ScoreBoard')
		con = Thread(target=self.connect_server())
		con.start()

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

		self.text = StringVar()
		self.text.set('off-line')
		self.status_bar = Label(self, 
			bg=self.back_ground,
			textvariable=self.text).pack(side=BOTTOM, expand=YES, fill=BOTH)

	def connect_server(self):
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket.bind(self.local_addr)
		while True:
			print(1)
			try:
				self.text.set('Connecting....')
				self.socket.connect(self.ser_addr)
				break
			except ConnectionRefusedError as e:
				self.text.set('Connect failed....')
			


	def check_client_status(self):
		pass

if __name__ == '__main__':
	App().mainloop()
