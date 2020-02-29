# -*- coding: utf-8 -*-
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

if __name__ == '__main__':
    root = Tk()
    app = Window(root)
    root.mainloop()
