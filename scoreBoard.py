#!/usr/bin/env python3
# -*- utf-8 -*-
from tkinter import *
from tkinter import ttk


class App(Frame):
    def __init__(self):
        self.back_ground = 'DimGray'
        Frame.__init__(self, bg=self.back_ground)
        self.pack(expand=YES, fill=BOTH)
        self.master.geometry('+200+200')
        self.master.minsize(width=800, height=300)
        # self.master.geometry('400x300')
        self.master.title('ScoreBoard')
        self.build_gui()

    def showinfo(self):
        pass

    def build_gui(self):
        self.tree.column('ID', width=50)
        self.tree.column('IP', width=100)
        self.tree.column('Port', width=50)
        self.tree.column('Score', width=50)
        self.tree.column('Status', width=50)

        self.tree.heading("ID", text="ID")  # 显示表头
        self.tree.heading("IP", text="IP")
        self.tree.heading("Port", text="Port")
        self.tree.heading("Score", text="Score")
        self.tree.heading("Status", text="Status")   # on-line off-line
        for i in range(8):
            self.tree.insert('', i, values=(i+1, 'Unknown', 'Unknown', 0, 'Off-line'))
        self.tree.pack(under=self.score_board, expand=YES, fill=BOTH)


if __name__ == '__main__':
    App().mainloop()
