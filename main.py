from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding = 100)
frm.grid()
ttk.Label(frm, text = "HELLO").grid(column = 0, row = 0)
ttk.Button(frm, text = "QUIT", command = root.destroy).grid(column = 0, row = 1)
btn = ttk.Button(frm, ...)
print(btn.configure().keys())
root.mainloop()
