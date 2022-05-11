#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *

"""
Создайте на холсте подобное изображение.
"""

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+300+300")
    root.title("Task4")
    c = Canvas(root, width=200, height=200, bg='white')
    c.pack()
    c.create_rectangle(50, 90, 140, 175,
                       fill='#7fc7ff', outline='#7fc7ff')
    c.create_polygon(30, 90, 160, 90, 95, 40,
                     fill='#7fc7ff', outline='#7fc7ff')
    c.create_oval(150, 10, 190, 50,
                  fill='yellow', outline='yellow')
    x = -20
    while x < 200:
        c.create_arc(x, 170, x + 40, 250, outline='green',
                     style=ARC, start=200, extent=-80,
                     width=2)
        x += 10
    root.mainloop()