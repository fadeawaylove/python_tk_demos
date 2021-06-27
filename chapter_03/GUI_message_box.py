"""
菜单栏 文件菜单 退出
"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg

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

# 标签框 tab2中
mighty2 = ttk.LabelFrame(tab2, text="The Snake")
mighty2.grid(column=0, row=0, padx=8, pady=4)

# 菜单栏
menu_bar = Menu(win)
win.config(menu=menu_bar)


def _quit():
    win.quit()
    win.destroy()
    exit()


def _msg_box():
    # msg.showinfo("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")
    # msg.showwarning("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")
    msg.showerror("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")


# 添加文件菜单
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# 添加帮助菜单
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msg_box)
menu_bar.add_cascade(label="Help", menu=help_menu)


def click_me():
    action.configure(text="Hello " + name.get() + number_chosen.get())
    action.configure(state="disabled")  # Disable the button widget


ttk.Label(mighty, text="Enter a name").grid(column=0, row=0, sticky=tk.W)

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

# 滚动框
scrol_w = 40
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=4, columnspan=3)
# scr.grid(column=0, sticky='WE', columnspan=3)

chvar_dis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chvar_dis, state="disabled")
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chvar_un = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="Unchecked", variable=chvar_un)
check2.deselect()
check2.grid(column=1, row=2, sticky=tk.W)

chvar_en = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chvar_en)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

colors = ["Blue", "Gold", "Red"]
rad_var = tk.IntVar()


def rad_call():
    red_cal = rad_var.get()
    mighty2.configure(text=colors[red_cal - 1])


for i in range(3):
    crad = tk.Radiobutton(mighty2, text=colors[i], variable=rad_var, value=i + 1, command=rad_call)
    crad.grid(column=i, row=3, sticky=tk.W, columnspan=3)

# Label Frame
label_frame = ttk.LabelFrame(mighty2, text="Labels in a Frame")
label_frame.grid(column=0, row=7, padx=20, pady=40)  # padx pady设置外边距

ttk.Label(label_frame, text="Label1").grid(column=0, row=0, )
ttk.Label(label_frame, text="Label2").grid(column=1, row=0, )
ttk.Label(label_frame, text="Label3").grid(column=2, row=0, )

win.mainloop()
