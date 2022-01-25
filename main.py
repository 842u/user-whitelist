from my_functions import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter

class MainWindow(tkinter.Tk):   #   TRY ANALIZE AND UNDERSTAND THIS

    def __init__(self) -> None:
        tkinter.Tk.__init__(self)

        version = "0.1.2"   #   major.minor.patch

        window_setup(self, title="LOGIN WINDOW", min_width=300, min_height=500, res=False)

        style_setup(self, txt_clr="#ffdd00", bg="black", fnt=("Bauhaus 93",14))     #   style_setup NEED TWEAKS -> MAKE DEFAULT VALUES
        style_setup(self, style="foot.", txt_clr="#5e5e5e", bg="black", fnt=("",8))

        frm_mw_1 = ttk.Frame(self)
        frm_mw_1.pack(fill=BOTH, expand=True)

        lbl_mw_1 = ttk.Label(frm_mw_1, text="HELLO STRANGER\n\nENTER MASTER PASSWORD:", justify=CENTER)
        lbl_mw_1.pack(pady=10)

        self.ent_mw_1 = ttk.Entry(frm_mw_1, show="*", justify=CENTER)
        self.ent_mw_1.pack(pady=10)

        btn_mw_1 = ttk.Button(frm_mw_1, text="LOG IN", command=self.on_click)
        btn_mw_1.pack()

        frm_mw_2 = ttk.Frame(self)
        frm_mw_2.pack(fill=BOTH, anchor=S)

        photo = tkinter.PhotoImage(file="img.png")
        logo = ttk.Label(frm_mw_2, image=photo)
        logo.pack(pady=50)
        logo.photo = photo  #   WITHOUT IT IMG DOESNT DISPLAY -> PhotoImage Garbage Collector PROBLEM 

        lbl_mw_ft = ttk.Label(frm_mw_2, text="842u", style="foot.TLabel")
        lbl_mw_ft.pack(side="right")

        lbl_mw_vr = ttk.Label(frm_mw_2, text=f"v.{version}", style="foot.TLabel",)
        lbl_mw_vr.pack(side="left")

    def on_click(self):

        password = "asd"

        if  self.ent_mw_1.get() == password:
            self.withdraw()
            self.acces_window = NewWindow(self)
            messagebox.showinfo("PASSWORD OK", "ACCES GRANTED")
        else:
            messagebox.showerror("PASSWORD CHECK", "WRONG PASSWORD")


class NewWindow(tkinter.Toplevel):
    
    def __init__(self, parent) -> None:
        tkinter.Toplevel.__init__(self, parent)

        window_setup(self, title="ACCES WINDOW", min_width=400, min_height=500)
        style_setup(self, txt_clr="#ffdd00", bg="black", fnt=("Bauhaus 93",16))
        style_setup(self, style="list.", txt_clr="#5e5e5e", bg="black", fnt=("Bauhaus 93",14))

        frm_aw_1 = ttk.Frame(self)
        frm_aw_1.pack(fill=BOTH, expand=True)

        frm_aw_1.columnconfigure(1, weight=0)
        frm_aw_1.columnconfigure(2, weight=1)
        frm_aw_1.rowconfigure(1, weight=0)
        frm_aw_1.rowconfigure(tuple(range(2,5)), weight=1)

        lbl_aw_d = ttk.Label(frm_aw_1, text="ADD USER TO WHITELIST")
        lbl_aw_d.grid(row=1, column=1, columnspan=2, pady=20)

        lbl_aw_n = ttk.Label(frm_aw_1, text="Name: ")
        lbl_aw_n.grid(row=2, column=1, sticky=W)
        self.ent_aw_n = ttk.Entry(frm_aw_1)     #   https://stackoverflow.com/questions/1101750/tkinter-attributeerror-nonetype-object-has-no-attribute-attribute-name
        self.ent_aw_n.grid(row=2, column=2, sticky=E+W, padx=20)

        lbl_aw_p = ttk.Label(frm_aw_1, text="Password: ")
        lbl_aw_p.grid(row=3, column=1, sticky=W)
        self.ent_aw_p = ttk.Entry(frm_aw_1)
        self.ent_aw_p.grid(row=3, column=2, sticky=E+W, padx=20)

        lbl_aw_e = ttk.Label(frm_aw_1, text="Email: ")
        lbl_aw_e.grid(row=4, column=1, sticky=W)
        self.ent_aw_e = ttk.Entry(frm_aw_1)
        self.ent_aw_e.grid(row=4, column=2, sticky=E+W, padx=20)

        btn_aw_au = ttk.Button(frm_aw_1, text="ADD USER", command=self.on_click)
        btn_aw_au.grid(row=5, column=1, pady=20)
        btn_aw_cls = ttk.Button(frm_aw_1, text="CLOSE APP", command=parent.destroy)
        btn_aw_cls.grid(row=5, column=2, pady=20)

        frm_aw_2 = ttk.Frame(self)
        frm_aw_2.pack(expand=True)

        with open("whitelist.txt", "r") as f:
            read_data = f.read()

        self.lbl_aw_dr = ttk.Label(frm_aw_2, text=read_data, style="list.TLabel")
        self.lbl_aw_dr.pack()

    def on_click(self):

        name = self.ent_aw_n.get()  #   MAKE "IF USER EXIST"
        password = self.ent_aw_p.get()
        email = self.ent_aw_e.get()

        if name=="" or password=="" or email=="":
            messagebox.showerror("DATA INCOMPLETE", "PLEASE ENTER ALL DATA")
        else:
            with open("whitelist.txt", "a+") as f:    #   MAYBE MAKE FUNCTION
                f.write(name+" // "+password+" // "+email+"\n")
            with open("whitelist.txt", "r") as f:
                data = f.read()
            self.lbl_aw_dr.config(text=data)


window = MainWindow()
window.mainloop()
