import tkinter as tk

win = tk.Tk()

double_data = tk.DoubleVar()
print(double_data.get())
double_data.set(2.4)
print(double_data.get())

add_doubles = 1.2222222222222222222 + double_data.get()
print(add_doubles)
print(type(add_doubles))
