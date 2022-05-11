#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *

"""
напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом поле приводит к перемещению текста
из него в список (экземпляр Listbox ). При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна
копироваться в текстовое поле.
"""

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200+90+90")
    root.title("Task2")

    ent1 = Entry()
    lb1 = Listbox()

    ent1.pack()
    lb1.pack()
    ent1.bind('<Return>', lambda e:  lb1.insert(0, ent1.get()))
    lb1.bind('<Double-Button-1>', lambda e: ent1.insert(0, lb1.get(lb1.curselection())))

    root.mainloop()