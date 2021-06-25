"""
检查按钮
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()


def click_me():
    action.configure(text="Hello " + name.get() + number_chosen.get())
    action.configure(state="disabled")  # Disable the button widget


ttk.Label(win, text="Enter a name").grid(column=0, row=0)

name = tk.StringVar()
name_entry = ttk.Entry(win, width=12, textvariable=name)
name_entry.grid(column=0, row=1)
name_entry.focus()

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text="Choose a number").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state="readonly")
number_chosen["values"] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chvar_dis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chvar_dis, state="disabled")
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chvar_un = tk.IntVar()
check2 = tk.Checkbutton(win, text="Unchecked", variable=chvar_un)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chvar_en = tk.IntVar()
check1 = tk.Checkbutton(win, text="Enabled", variable=chvar_en)
check1.select()
check1.grid(column=2, row=2, sticky=tk.W)

win.mainloop()
