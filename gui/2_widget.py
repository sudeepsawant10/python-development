"""
We have to invoke class for creating particular widgets.
use interactive mode for more flexible
"""
import tkinter as tk

win = tk.Tk()
win.title("Python Gui")
win.geometry("300x300")
# win.resizable(0, 0)  # To avoid maximize and minimize
# print(win.state())  # status of window
win.config(bg="yellow")

lbl = tk.Label(win, text="Hello")
lbl.config(bg="red")
lbl.config(fg="yellow")
lbl.pack()
# win.destroy()         #To destroy window and object also
win.mainloop()
