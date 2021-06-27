"""
菜单栏 文件菜单 退出
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk()

win.title("Python GUI")
tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")
tab_control.add(tab2, text="Tab 2")
tab_control.pack(expand=1, fill='both')

# 标签框 tab1中
mighty = ttk.LabelFrame(tab1, text="Mighty Python")
mighty.grid(column=0, row=0, padx=8, pady=4)

# 标签 在标签框中
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky="W")
win.mainloop()
