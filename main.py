import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def btn_pressed():
    messagebox.showinfo(":) Button status message :)", "Button has been pressed.\n  ✌.|•͡˘‿•͡˘|.✌")

root = Tk()
root.title("842u")

width = 300
height = 450
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()
x_coord = int((screen_width/2) - (width/2))
y_coord = int((screen_heigth/2) - (height/2))
root.geometry(f"{width}x{height}+{x_coord}+{y_coord}")
root.minsize(width,height)

style = ttk.Style()
style.configure("N.TFrame", background="black")
style.configure("N.TLabel", foreground="#ffe600", background="black", font=("",16), justify=CENTER)
style.configure("WM.TLabel", foreground="#2e2e2e", background="black", font=("",10), justify=CENTER)
style.configure("N.TButton", foreground="black", background="black")

frm_1 = ttk.Frame(root, style="N.TFrame")
frm_1.pack(fill=BOTH, expand=True)

txt = ttk.Label(frm_1, text="Hello\n\nEnter master password:", style="N.TLabel")
txt.pack(anchor=CENTER, pady=10)

ent = ttk.Entry(frm_1, show="*", justify=CENTER, width=30)
ent.pack(pady=20, anchor=CENTER)

btn_confirm = ttk.Button(frm_1, text="CONFIRM", style="N.TButton", command=btn_pressed)
btn_confirm.pack(anchor=CENTER)

photo = tkinter.PhotoImage(file="img.png")
frm_2 = ttk.Frame(frm_1, style="N.TFrame")
frm_2.pack(anchor=S, expand=True)

logo = ttk.Label(frm_2, image=photo, style="N.TLabel")
logo.pack(fill=BOTH)

txt_wm = ttk.Label(frm_1, text="842u", justify="right", style="WM.TLabel")
txt_wm.pack(fill=BOTH, side="right")

root.mainloop()
