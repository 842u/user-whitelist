import tkinter
import pandas as pd
from tkinter import *
from tkinter import ttk


def window_setup(window_name, title="new window", min_width=100, min_height=100, res=True):
    window_name.title(f"{title}")

    window_name.min_width = min_width
    window_name.min_height = min_height

    if res == False:
        window_name.resizable(0,0)

    screen_width = window_name.winfo_screenwidth()
    screen_height = window_name.winfo_screenheight()
    x_coord = int((screen_width/2) - (min_width/2))
    y_coord = int((screen_height/2) - (min_height/2))
    window_name.minsize(window_name.min_width,window_name.min_height)
    window_name.geometry(f"{window_name.min_width}x{window_name.min_height}+{x_coord}+{y_coord}")

def style_setup(window_name, style="", txt_clr="black", bg="white", fnt=("",14),):
    window_name.style = ttk.Style()

    window_name.style.configure(style+"TLabel", foreground=txt_clr, background=bg, font=fnt)

    widgets = ["TFrame", "TButton"]
    for i in widgets:
        window_name.style.configure(style+i, background=bg)

def main_window_layout(self):
    window_setup(self, title="LOGIN WINDOW", min_width=300, min_height=500, res=False)
    style_setup(self, txt_clr="#ffdd00", bg="black", fnt=("Bauhaus 93",14))
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
    logo.photo = photo

    lbl_mw_ft = ttk.Label(frm_mw_2, text="842u", style="foot.TLabel")
    lbl_mw_ft.pack(side="right")

    lbl_mw_vr = ttk.Label(frm_mw_2, text=f"v.{self.version}", style="foot.TLabel",)
    lbl_mw_vr.pack(side="left")

def acces_window_layout(self, parent):
    window_setup(self, title="ACCES WINDOW", min_width=450, min_height=700)

    # FRAME
    self.frm_aw_1 = ttk.Frame(self)
    self.frm_aw_1.pack(fill=BOTH, expand=True)
    self.frm_aw_1.columnconfigure(1, weight=0)
    self.frm_aw_1.columnconfigure(2, weight=1)
    self.frm_aw_1.rowconfigure(1, weight=0)
    self.frm_aw_1.rowconfigure(tuple(range(2,5)), weight=1)

    self.frm_aw_2 = ttk.Frame(self)
    self.frm_aw_2.pack(fill=BOTH, expand=True)

    # LABEL
    self.lbl_aw_d = ttk.Label(self.frm_aw_1, text="ADD USER TO WHITELIST")
    self.lbl_aw_d.grid(row=1, column=1, columnspan=4, pady=20)

    self.lbl_aw_n = ttk.Label(self.frm_aw_1, text="User : ")
    self.lbl_aw_n.grid(row=2, column=1, sticky=W, padx=20)

    self.lbl_aw_p = ttk.Label(self.frm_aw_1, text="Password : ")
    self.lbl_aw_p.grid(row=3, column=1, sticky=W, padx=20)

    self.lbl_aw_e = ttk.Label(self.frm_aw_1, text="Email : ")
    self.lbl_aw_e.grid(row=4, column=1, sticky=W, padx=20)

    # ENTRY
    self.ent_aw_n = ttk.Entry(self.frm_aw_1)     #   https://stackoverflow.com/questions/1101750/tkinter-attributeerror-nonetype-object-has-no-attribute-attribute-name
    self.ent_aw_n.grid(row=2, column=2, columnspan=3, sticky=E+W, padx=20)

    self.ent_aw_p = ttk.Entry(self.frm_aw_1)
    self.ent_aw_p.grid(row=3, column=2, columnspan=3, sticky=E+W, padx=20)

    self.ent_aw_e = ttk.Entry(self.frm_aw_1)
    self.ent_aw_e.grid(row=4, column=2, columnspan=3, sticky=E+W, padx=20)

    # BUTTON
    self.btn_aw_au = ttk.Button(self.frm_aw_1, text="ADD USER", command=self.on_click_add)
    self.btn_aw_au.grid(row=5, column=1, sticky=W, pady=20, padx=20)

    self.btn_aw_au = ttk.Button(self.frm_aw_1, text="DELETE USER", command=self.on_click_del)
    self.btn_aw_au.grid(row=5, column=2, sticky=W, pady=20)

    self.btn_aw_au = ttk.Button(self.frm_aw_1, text="EDIT USER", command=self.on_click_edit)
    self.btn_aw_au.grid(row=5, column=3, sticky=E, pady=20)

    self.btn_aw_cls = ttk.Button(self.frm_aw_1, text="CLOSE", command=parent.destroy)
    self.btn_aw_cls.grid(row=5, column=4, sticky=E, pady=20, padx=20)

    # TREEVIEW
    self.tw_aw_1 = ttk.Treeview(self.frm_aw_2, selectmode='browse')
    self.tw_aw_1.pack()

    self.tw_aw_1['columns'] = ('index', 'name', 'password', 'email')

    self.tw_aw_1.column("#0", width=0, stretch=NO)
    self.tw_aw_1.column("index", anchor=CENTER, width=80)
    self.tw_aw_1.column("name", anchor=CENTER, width=80)
    self.tw_aw_1.column("password", anchor=CENTER, width=80)
    self.tw_aw_1.column("email", anchor=CENTER, width=80)

    self.tw_aw_1.heading("#0", text="",  anchor=CENTER)
    self.tw_aw_1.heading("index", text="#", anchor=CENTER)
    self.tw_aw_1.heading("name", text="NAME", anchor=CENTER)
    self.tw_aw_1.heading("password", text="PASSWORD", anchor=CENTER)
    self.tw_aw_1.heading("email", text="EMAIL", anchor=CENTER)

def user_window_layout(self):
    window_setup(self, title="USER EDIT", min_width=400, min_height=250)

    # FRAME
    self.frm_uw_1 = ttk.Frame(self)
    self.frm_uw_1.pack(fill=BOTH, expand=True)
    self.frm_uw_1.columnconfigure(1, weight=0)
    self.frm_uw_1.columnconfigure(2, weight=1)
    self.frm_uw_1.rowconfigure(1, weight=0)
    self.frm_uw_1.rowconfigure(tuple(range(2,5)), weight=1)

    self.frm_uw_2 = ttk.Frame(self)
    self.frm_uw_2.pack(fill=BOTH)
    self.frm_uw_2.columnconfigure(1, weight=0)
    self.frm_uw_2.columnconfigure(2, weight=1)
    self.frm_uw_2.rowconfigure(1, weight=0)
    self.frm_uw_2.rowconfigure(tuple(range(2,5)), weight=1)

    # TREEVIEW
    self.tw_uw_1 = ttk.Treeview(self.frm_uw_1, selectmode='none', height=1)
    self.tw_uw_1.grid(row=1, column=1, columnspan=4)

    self.tw_uw_1['columns'] = ('index', 'name', 'password', 'email')

    self.tw_uw_1.column("#0", width=0, stretch=NO)
    self.tw_uw_1.column("index", anchor=CENTER, width=25)
    self.tw_uw_1.column("name", anchor=CENTER, width=100)
    self.tw_uw_1.column("password", anchor=CENTER, width=100)
    self.tw_uw_1.column("email", anchor=CENTER, width=100)

    self.tw_uw_1.heading("#0", text="",  anchor=CENTER)
    self.tw_uw_1.heading("index", text="#", anchor=CENTER)
    self.tw_uw_1.heading("name", text="NAME", anchor=CENTER)
    self.tw_uw_1.heading("password", text="PASSWORD", anchor=CENTER)
    self.tw_uw_1.heading("email", text="EMAIL", anchor=CENTER)

    # LABEL
    self.lbl_uw_n = ttk.Label(self.frm_uw_1, text="User : ")
    self.lbl_uw_n.grid(row=2, column=1, sticky=W, padx=20)

    self.lbl_uw_p = ttk.Label(self.frm_uw_1, text="Password : ")
    self.lbl_uw_p.grid(row=3, column=1, sticky=W, padx=20)

    self.lbl_uw_e = ttk.Label(self.frm_uw_1, text="Email : ")
    self.lbl_uw_e.grid(row=4, column=1, sticky=W, padx=20)

    # ENTRY
    self.ent_uw_n = ttk.Entry(self.frm_uw_1)
    self.ent_uw_n.grid(row=2, column=2, sticky=E+W, padx=20)

    self.ent_uw_p = ttk.Entry(self.frm_uw_1)
    self.ent_uw_p.grid(row=3, column=2, sticky=E+W, padx=20)

    self.ent_uw_e = ttk.Entry(self.frm_uw_1)
    self.ent_uw_e.grid(row=4, column=2, sticky=E+W, padx=20)

    # BUTTON
    self.btn_uw_s = ttk.Button(self.frm_uw_2, text="SAVE")
    self.btn_uw_s.grid(row=1, column=1, padx=20, pady=20)

    self.btn_uw_r = ttk.Button(self.frm_uw_2, text="RESET")
    self.btn_uw_r.grid(row=1, column=2, padx=20, pady=20)

    self.btn_uw_c = ttk.Button(self.frm_uw_2, text="CLOSE", command=self.destroy)
    self.btn_uw_c.grid(row=1, column=3, padx=20, pady=20)
