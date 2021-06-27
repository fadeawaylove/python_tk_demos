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


win.mainloop()
