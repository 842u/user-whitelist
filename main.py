from textwrap import fill
import tkinter
from tkinter import *
from tkinter import ttk
from turtle import heading, right

root = Tk()
root.title("842u")

w = 300
h = 450
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x_coord = int((sw/2) - (w/2))
y_coord = int((sh/2) - (h/2))
root.geometry(f"{w}x{h}+{x_coord}+{y_coord}")
root.resizable(height=False, width=False)

style = ttk.Style()
# style.configure("style_name.TLabel", foreground = "#00ff44", background = "black")
style.configure("TLabel", foreground="#ffe600", background="black", font=("",16), justify=CENTER)
style.configure("TButton", foreground="black", background="black")

frm = ttk.Frame(root, style="TLabel")
# frm.pack(fill=BOTH, expand=False)
frm.pack(fill=BOTH, expand=True)

txt = ttk.Label(frm, text="Hello\n\nEnter master password:")
txt.pack(anchor=CENTER, pady=10)

ent = ttk.Entry(frm, show="*", justify=CENTER, width=30)
ent.pack(pady=20, anchor=CENTER)

btn = ttk.Button(frm, text="CONFIRM", command=root.destroy) ####### CHANGE FROM QUIT TO CONFIRM
btn.pack(anchor=CENTER)

photo = tkinter.PhotoImage(file="img.png")
# logo = ttk.Label(root, text="asd", image=photo, style="TLabel")
frm2 = ttk.Frame(frm, style="TLabel")
frm2.pack(anchor=S, expand=True)

logo = ttk.Label(frm2, image=photo, style="TLabel")
logo.pack(fill=BOTH)

wm = ttk.Label(frm, text="842u", justify="right")
wm.pack(fill=BOTH, side="right")


root.mainloop()
