# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:33:37 2022

@author: eichc
"""

from tkinter import *

# class MyApp(object):
#     def __init__(self, parent):
#         self.main_frame = Frame(parent)
#         self.main_frame.pack()

#         self.top_frame = Frame(self.main_frame)
#         self.top_frame.pack(side=TOP)
#         self.bottom_frame = Frame(self.main_frame)
#         self.bottom_frame.pack(side=BOTTOM)

#         self.button1 = Button(self.top_frame, text="Top 1")
#         self.button1.pack(side=LEFT)
#         self.button2 = Button(self.top_frame, text="Top 2")
#         self.button2.pack(side=RIGHT)
#         self.button3 = Button(self.bottom_frame, text="Bottom 1")
#         self.button3.pack(side=LEFT)
#         self.button4 = Button(self.bottom_frame, text="Bottom 2")
#         self.button4.pack(side=RIGHT)

class MyApp(object):
    def __init__(self, parent):
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.button = Button(self.main_frame, text="Quit", command=self.terminate_program)
        self.button.configure(width=12, padx="4m", pady="4m")
        self.button.pack()

    def terminate_program(self):
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    root.mainloop()