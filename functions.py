import tkinter
from tkinter import *
from tkinter import ttk

def window_setup(window_master, title='new window', min_width=100, min_height=100, res=True):
    window_master.title(f'{title}')

    window_master.min_width = min_width
    window_master.min_height = min_height

    if res == False: window_master.resizable(0,0)

    screen_width = window_master.winfo_screenwidth()
    screen_height = window_master.winfo_screenheight()

    x_pos = int((screen_width/2) - (min_width/2))
    y_pos = int((screen_height/2) - (min_height/2))
    
    window_master.minsize(window_master.min_width,window_master.min_height)
    window_master.geometry(f'{window_master.min_width}x{window_master.min_height}+{x_pos}+{y_pos}')

def style_setup(self, style='', txt_clr='black', bg='white', fnt=('',14),):
    self.style = ttk.Style()

    self.style.configure(style+'TLabel', foreground=txt_clr, background=bg, font=fnt)

    widgets = ['TFrame', 'TButton']
    for i in widgets:
        self.style.configure(style+i, background=bg)

def update_treeview(treeview, data):
    treeview.delete(*treeview.get_children())

    for x in range(len(data)):
        data.loc[x,'index'] = x+1
        treeview.insert(parent='', index='end', iid=x, text='', 
            values=(
                x+1,
                data.loc[x,'name'],
                data.loc[x,'password'],
                data.loc[x,'email']
            )
        )

def login_window_layout(self):
    #   SETUP
    window_setup(self.login_window_master, 'LOGIN WINDOW', 300, 500)
    style_setup(self, txt_clr='#ffdd00', bg='black', fnt=('Bauhaus 93',14))
    style_setup(self, style='foot.', txt_clr='#5e5e5e', bg='black', fnt=('',8))

    #   FRAME
    self.lw_frm_1 = ttk.Frame(self)
    self.lw_frm_1.pack(fill=BOTH, expand=True)
    self.lw_frm_2 = ttk.Frame(self)
    self.lw_frm_2.pack(fill=BOTH, anchor=S)

    #   IMAGE
    photo = tkinter.PhotoImage(file='img.png')
    self.logo = ttk.Label(self.lw_frm_2, image=photo)
    self.logo.pack(pady=50)
    self.logo.photo = photo

    #   LABEL
    self.lw_lbl_top = ttk.Label(self.lw_frm_1, text='HELLO STRANGER\n\nENTER MASTER PASSWORD:', justify=CENTER)
    self.lw_lbl_top.pack(pady=10)
    self.lw_lbl_ft = ttk.Label(self.lw_frm_2, text='842u', style='foot.TLabel')
    self.lw_lbl_ft.pack(side='right')
    self.lw_lbl_vr = ttk.Label(self.lw_frm_2, text=f'{self.version}', style='foot.TLabel',)
    self.lw_lbl_vr.pack(side='left')

    #   ENTRY
    self.lw_ent_p = ttk.Entry(self.lw_frm_1, show='*', justify=CENTER)
    self.lw_ent_p.pack(pady=10)

    #   BUTTON
    self.lw_btn_li = ttk.Button(self.lw_frm_1, text='LOG IN', command=self.on_click_btn_li)
    self.lw_btn_li.pack()

def acces_window_layout(self):
    #   SETUP
    window_setup(self.acces_window_master, 'ACCES WINDOW', 600, 700)

    #   FRAME
    self.aw_frm_1 = ttk.Frame(self)
    self.aw_frm_1.pack(fill=BOTH, expand=True)

    self.aw_frm_a = ttk.Frame(self)
    self.aw_frm_a.pack(fill=BOTH, expand=True)

    self.aw_frm_b = ttk.Frame(self.aw_frm_a, width=10)
    self.aw_frm_b.pack(fill=BOTH, side='right')

    self.aw_frm_n = ttk.Frame(self)
    self.aw_frm_n.pack(fill=BOTH, expand=True)

    self.aw_frm_p = ttk.Frame(self)
    self.aw_frm_p.pack(fill=BOTH, expand=True)

    self.aw_frm_e = ttk.Frame(self)
    self.aw_frm_e.pack(fill=BOTH, expand=True)

    self.aw_frm_2 = ttk.Frame(self)
    self.aw_frm_2.pack(fill=BOTH, expand=True)

    #   LABEL
    self.aw_lbl_top = ttk.Label(self.aw_frm_1, justify=CENTER, text='WHITELIST')
    self.aw_lbl_top.pack(pady=10)

    self.aw_lbl_n = ttk.Label(self.aw_frm_n, text='User :', width=10)
    self.aw_lbl_n.pack(side='left', padx=20)

    self.aw_lbl_p = ttk.Label(self.aw_frm_p, text='Password :', width=10)
    self.aw_lbl_p.pack(side='left', padx=20)

    self.aw_lbl_e = ttk.Label(self.aw_frm_e, text='Email :', width=10)
    self.aw_lbl_e.pack(side='left', padx=20)

    #   ENTRY
    self.aw_ent_n = ttk.Entry(self.aw_frm_n)
    self.aw_ent_n.pack(side='right', padx=20, expand=True, fill=X)

    self.aw_ent_p = ttk.Entry(self.aw_frm_p)
    self.aw_ent_p.pack(side='right', padx=20, expand=True, fill=X)

    self.aw_ent_e = ttk.Entry(self.aw_frm_e)
    self.aw_ent_e.pack(side='right', padx=20, expand=True, fill=X)

    #   BUTTON
    self.aw_btn_au = ttk.Button(self.aw_frm_2, text='ADD USER', command=self.on_click_btn_au)
    self.aw_btn_au.pack(padx=20)

    self.aw_btn_eu = ttk.Button(self.aw_frm_b, text='EDIT USER', width=15, command=self.on_click_btn_eu)
    self.aw_btn_eu.pack(padx=20)

    self.aw_btn_du = ttk.Button(self.aw_frm_b, text='DELETE USER', width=15, command=self.on_click_btn_du)
    self.aw_btn_du.pack(padx=20, pady=20)

    #   TREEVIEW
    self.aw_tw_1 = ttk.Treeview(self.aw_frm_a, selectmode='browse')
    self.aw_tw_1.pack(padx=20, fill=BOTH, expand=True, side='left')

    self.aw_tw_1['columns'] = ('index', 'name', 'password', 'email')

    self.aw_tw_1.column('#0', width=0, stretch=NO)
    self.aw_tw_1.column('index', anchor=CENTER, width=30, stretch=NO)
    self.aw_tw_1.column('name', anchor=CENTER, width=80)
    self.aw_tw_1.column('password', anchor=CENTER, width=80)
    self.aw_tw_1.column('email', anchor=CENTER, width=80)

    self.aw_tw_1.heading('#0', text='',  anchor=CENTER)
    self.aw_tw_1.heading('index', text='#', anchor=CENTER)
    self.aw_tw_1.heading('name', text='NAME', anchor=CENTER)
    self.aw_tw_1.heading('password', text='PASSWORD', anchor=CENTER)
    self.aw_tw_1.heading('email', text='EMAIL', anchor=CENTER)

def user_window_layout(self, user):
    #   SETUP
    window_setup(self.user_window_master, f'#{user+1} USER WINDOW', 400, 300)

    #   FRAME
    self.uw_frm_1 = ttk.Frame(self)
    self.uw_frm_1.pack(fill=BOTH, expand=True)
    self.uw_frm_1.columnconfigure(1, weight=0)
    self.uw_frm_1.columnconfigure(2, weight=1)
    self.uw_frm_1.rowconfigure(1, weight=0)
    self.uw_frm_1.rowconfigure(tuple(range(2,5)), weight=1)

    self.uw_frm_2 = ttk.Frame(self)
    self.uw_frm_2.pack(fill=BOTH)
    self.uw_frm_2.columnconfigure(1, weight=0)
    self.uw_frm_2.columnconfigure(2, weight=1)
    self.uw_frm_2.rowconfigure(1, weight=0)
    self.uw_frm_2.rowconfigure(tuple(range(2,5)), weight=1)

    #   TREEVIEW
    self.uw_tw_1 = ttk.Treeview(self.uw_frm_1, selectmode='none', height=1)
    self.uw_tw_1.grid(row=1, column=1, columnspan=4)

    self.uw_tw_1['columns'] = ('index', 'name', 'password', 'email')

    self.uw_tw_1.column('#0', width=0, stretch=NO)
    self.uw_tw_1.column('index', anchor=CENTER, width=25)
    self.uw_tw_1.column('name', anchor=CENTER, width=100)
    self.uw_tw_1.column('password', anchor=CENTER, width=100)
    self.uw_tw_1.column('email', anchor=CENTER, width=100)

    self.uw_tw_1.heading('#0', text='',  anchor=CENTER)
    self.uw_tw_1.heading('index', text='#', anchor=CENTER)
    self.uw_tw_1.heading('name', text='NAME', anchor=CENTER)
    self.uw_tw_1.heading('password', text='PASSWORD', anchor=CENTER)
    self.uw_tw_1.heading('email', text='EMAIL', anchor=CENTER)

    #   LABEL
    self.uw_lbl_n = ttk.Label(self.uw_frm_1, text='User : ')
    self.uw_lbl_n.grid(row=2, column=1, sticky=W, padx=20)

    self.uw_lbl_p = ttk.Label(self.uw_frm_1, text='Password : ')
    self.uw_lbl_p.grid(row=3, column=1, sticky=W, padx=20)

    self.uw_lbl_e = ttk.Label(self.uw_frm_1, text='Email : ')
    self.uw_lbl_e.grid(row=4, column=1, sticky=W, padx=20)

    #   ENTRY
    self.uw_ent_n = ttk.Entry(self.uw_frm_1)
    self.uw_ent_n.grid(row=2, column=2, sticky=E+W, padx=20)

    self.uw_ent_p = ttk.Entry(self.uw_frm_1)
    self.uw_ent_p.grid(row=3, column=2, sticky=E+W, padx=20)

    self.uw_ent_e = ttk.Entry(self.uw_frm_1)
    self.uw_ent_e.grid(row=4, column=2, sticky=E+W, padx=20)

    #   BUTTON
    self.uw_btn_s = ttk.Button(self.uw_frm_2, text='SAVE', command=self.on_click_btn_s)
    self.uw_btn_s.grid(row=1, column=1, padx=20, pady=20)

    self.uw_btn_r = ttk.Button(self.uw_frm_2, text='RESET', command=self.on_click_btn_r)
    self.uw_btn_r.grid(row=1, column=2, padx=20, pady=20)
