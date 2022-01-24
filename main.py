from my_functions import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
class MakeWindow(tkinter.Tk):   #   TRY ANALIZE AND UNDERSTAND THIS

    def __init__(self) -> None:
        tkinter.Tk.__init__(self)

        window_setup(self, title="LOGIN WINDOW", min_width=300, min_height=500, res=True)

        style_setup(self, txt_clr="#ffdd00", bg="black", fnt=("Bauhaus 93",14))     #   style_setup NEED TWEAKS -> MAKE DEFAULT VALUES
        style_setup(self, style="foot.", txt_clr="#5e5e5e", bg="black", fnt=("",8))

        frm_1 = ttk.Frame(self)
        frm_1.pack(fill=BOTH, expand=True)

        lbl_1 = ttk.Label(frm_1, text="HELLO STRANGER\n\nENTER MASTER PASSWORD:", justify=CENTER)
        lbl_1.pack(pady=10)

        self.ent_1 = ttk.Entry(frm_1, show="*", justify=CENTER)
        self.ent_1.pack(pady=10)

        btn_1 = ttk.Button(frm_1, text="LOG IN", command=self.on_click)
        btn_1.pack()

        frm_2 = ttk.Frame(self)
        frm_2.pack(fill=BOTH, anchor=S)

        photo = tkinter.PhotoImage(file="img.png")
        logo = ttk.Label(frm_2, image=photo)
        logo.pack(pady=50)
        logo.photo = photo  #   WITHOUT IT IMG DOESNT DISPLAY -> PhotoImage Garbage Collector PROBLEM 

        lbl_ft = ttk.Label(frm_2, text="842u", style="foot.TLabel")
        lbl_ft.pack(side="right")

        lbl_vr = ttk.Label(frm_2, text="v.0.1.1", style="foot.TLabel",)
        lbl_vr.pack(side="left")

    def on_click(self):
        if  self.ent_1.get() == "asd":
            messagebox.showinfo("PASSWORD CHECK", "PASSWORD OK")
        else:
            messagebox.showerror("PASSWORD CHECK", "WRONG PASSWORD")


window = MakeWindow()
window.mainloop()
