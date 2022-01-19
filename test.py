from my_functions import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter

class MakeWindow(tkinter.Tk):   #   TRY ANALIZE AND UNDERSTAND THIS

    def __init__(self) -> None:
        tkinter.Tk.__init__(self)

        window_setup(self, title="LOGIN SCREEN", min_width=300, min_height=500, res=True)

        style_setup(self, fg="#eb4034", bg="#000000")   #   NEED TWEAKS - MAKE DEFAULT VALUES

        wl_frm_1 = ttk.Frame(self)
        wl_frm_1.pack(fill=BOTH, expand=True)

        wl_lbl_1 = ttk.Label(wl_frm_1, text="HELLO")
        wl_lbl_1.pack()

        self.wl_ent_1 = ttk.Entry(wl_frm_1)
        self.wl_ent_1.pack()

        wl_btn_1 = ttk.Button(wl_frm_1, text="TRY", command=self.on_click)
        wl_btn_1.pack()

    def on_click(self):
        if  self.wl_ent_1.get() == "asd":
            messagebox.showinfo("PASSWORD CHECK", "PASSWORD OK")
        else:
            messagebox.showerror("PASSWORD CHECK", "WRONG PASSWORD")


window = MakeWindow()
window.mainloop()
