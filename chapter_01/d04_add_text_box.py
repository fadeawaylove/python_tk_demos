import time
import tkinter as tk
from tkinter import ttk

win = tk.Tk()


def click_me():
    action.configure(text="Hello " + name.get())


ttk.Label(win, text="Enter a name").grid(column=0, row=0)

name = tk.StringVar()
name_entry = ttk.Entry(win, width=12, textvariable=name)
name_entry.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)

win.mainloop()
