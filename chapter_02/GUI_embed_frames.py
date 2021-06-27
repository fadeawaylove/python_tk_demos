"""
嵌入式框架
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

mighty = ttk.LabelFrame(win, text="Mighty Python")
mighty.grid(column=0, row=0, padx=8, pady=4)


def click_me():
    action.configure(text="Hello " + name.get() + number_chosen.get())
    action.configure(state="disabled")  # Disable the button widget


ttk.Label(mighty, text="Enter a name").grid(column=0, row=0, sticky=tk.W)

# 滚动框
scrol_w = 40
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=4, columnspan=3)

name = tk.StringVar()
name_entry = ttk.Entry(mighty, width=12, textvariable=name)
name_entry.grid(column=0, row=1, sticky=tk.W)
name_entry.focus()

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

ttk.Label(mighty, text="Choose a number").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state="readonly")
number_chosen["values"] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

chvar_dis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chvar_dis, state="disabled")
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chvar_un = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="Unchecked", variable=chvar_un)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chvar_en = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chvar_en)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

colors = ["Blue", "Gold", "Red"]
rad_var = tk.IntVar()


def rad_call():
    red_cal = rad_var.get()
    win.configure(background=colors[red_cal - 1])


for i in range(3):
    crad = tk.Radiobutton(mighty, text=colors[i], variable=rad_var, value=i + 1, command=rad_call)
    crad.grid(column=i, row=3, sticky=tk.W, columnspan=3)

# Label Frame
label_frame = ttk.LabelFrame(mighty, text="Labels in a Frame")
label_frame.grid(column=0, row=7, padx=20, pady=40)  # padx pady设置外边距

ttk.Label(label_frame, text="Label1").grid(column=0, row=0, )
ttk.Label(label_frame, text="Label2").grid(column=0, row=1, )
ttk.Label(label_frame, text="Label3").grid(column=0, row=2, )
# 左对齐
# for child in label_frame.mightyfo_children():
#     child.grid_configure(padx=8, pady=4)
#     pass

win.mainloop()
