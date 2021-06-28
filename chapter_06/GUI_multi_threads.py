"""
画布
"""
import tkinter as tk
from time import sleep
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
from tkinter import messagebox as msg

from chapter_04.GUI_tooltip import create_ToolTip
from threading import Thread


class OOP:

    def __init__(self):
        # create instance
        self.win = tk.Tk()
        # add a title
        self.win.title("Python GUI")
        self.create_widgets()

    def click_me(self):
        self.action.configure(text="Hello " + self.name.get() + self.number_chosen.get())

        self.create_thread()

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def _msg_box(self):
        # msg.showinfo("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")
        # msg.showwarning("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")
        # msg.showerror("Python Message Info Box", "A Python GUI created using tkinter:\nThe year is 2021.")
        answer = msg.askyesnocancel("Python Message Multi Choice Box",
                                    "Are you sure you really wish to do this?")

    def _spin(self):
        value = self.spin.get()
        # print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    def rad_call(self):
        red_cal = self.rad_var.get()
        self.mighty2.configure(text=self.colors[red_cal - 1])

    def method_in_a_thread(self):
        print("Hi, How are you?")
        for i in range(10):
            sleep(1)
            self.scr.insert(tk.INSERT, str(i) + '\n')  # Disable the button widget

    def create_thread(self):
        self.run_thread = Thread(target=self.method_in_a_thread)
        self.run_thread.setDaemon()
        self.run_thread.start()
        print(self.run_thread)

    def create_widgets(self):
        tab_control = ttk.Notebook(self.win)
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
        self.mighty2 = mighty2

        # 菜单栏
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # 添加文件菜单
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='New')
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self._quit)
        menu_bar.add_cascade(label='File', menu=file_menu)

        # 添加帮助菜单
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msg_box)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        ttk.Label(mighty, text="Enter a name").grid(column=0, row=0, sticky=tk.W)

        self.name = tk.StringVar()
        name_entry = ttk.Entry(mighty, width=24, textvariable=self.name)
        name_entry.grid(column=0, row=1, sticky=tk.W)
        name_entry.focus()

        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)

        ttk.Label(mighty, text="Choose a number").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state="readonly")
        self.number_chosen["values"] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        # spin box
        self.spin = Spinbox(mighty, from_=0, to=10, width=5, command=self._spin)
        self.spin.grid(column=0, row=3)

        create_ToolTip(self.spin, "This is a Spin Control.")

        # 滚动框
        scrol_w = 80
        scrol_h = 10
        scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr = scr
        scr.grid(column=0, row=4, columnspan=3)
        # scr.grid(column=0, sticky='WE', columnspan=3)
        create_ToolTip(scr, "This is a ScrolledText Widget.")

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
        self.colors = colors
        rad_var = tk.IntVar()
        self.rad_var = rad_var

        for i in range(3):
            crad = tk.Radiobutton(mighty2, text=colors[i], variable=rad_var, value=i + 1, command=self.rad_call)
            crad.grid(column=i, row=3, sticky=tk.W, columnspan=3)

        # Label Frame
        label_frame = ttk.LabelFrame(mighty2, text="Labels in a Frame")
        label_frame.grid(column=0, row=7, padx=20, pady=40)  # padx pady设置外边距

        ttk.Label(label_frame, text="Label1").grid(column=0, row=0, )
        ttk.Label(label_frame, text="Label2").grid(column=1, row=0, )
        ttk.Label(label_frame, text="Label3").grid(column=2, row=0, )

        self.win.mainloop()


oop = OOP()
run_thread = Thread(target=oop.method_in_a_thread)
oop.create_widgets()
