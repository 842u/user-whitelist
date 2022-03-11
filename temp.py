import tkinter
import pandas as pd
from functions import *
from tkinter import *
from tkinter import messagebox

class LoginWindow(tkinter.Tk):
    version = "0.2.0"
    master_password = "123"
    max_users = 10

    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        main_window_layout(self)

    def on_click(self):
        if  self.ent_mw_1.get() == self.master_password:
            self.withdraw()
            messagebox.showinfo("PASSWORD OK", "ACCES GRANTED")
            AccesWindow(self)
        else:
            messagebox.showerror("PASSWORD CHECK", "WRONG PASSWORD")


class AccesWindow(tkinter.Toplevel):
    selected_user = None

    def __init__(self, parent) -> None:
        tkinter.Toplevel.__init__(self, parent)
        acces_window_layout(self, parent)

        # UPDATE TREEVIEW
        self.tw_aw_1.delete(*self.tw_aw_1.get_children())
        for x in range(len(self.df)):
            self.df.loc[x,'index'] = x+1
            self.tw_aw_1.insert(parent='', index='end', iid=x, text='', 
                values=(
                    x+1,
                    self.df.loc[x,'name'],
                    self.df.loc[x,'password'],
                    self.df.loc[x,'email']
                )
            )

    def on_click_add(self):
        user_name = self.ent_aw_n.get()
        user_password = self.ent_aw_p.get()
        user_email = self.ent_aw_e.get()

        actual_number_of_users = len(self.df)

        if user_name=="" or user_password=="" or user_email=="":

            messagebox.showerror("DATA INCOMPLETE", "PLEASE ENTER ALL DATA")

        elif actual_number_of_users < LoginWindow.max_users:

            self.df.loc[-1] = [actual_number_of_users+1, user_name, user_password, user_email]
            self.df = self.df.reset_index(drop=True)

            x = len(self.df)

            self.tw_aw_1.insert(parent='', index='end', iid=x, text='', 
                values=(
                    self.df.loc[x-1, 'index'],
                    self.df.loc[x-1,'name'],
                    self.df.loc[x-1,'password'],
                    self.df.loc[x-1,'email']
                )
            )

            self.df.to_csv('whitelist.csv', index=False)

            # UPDATE TREEVIEW
            self.tw_aw_1.delete(*self.tw_aw_1.get_children())
            for x in range(len(self.df)):
                self.df.loc[x,'index'] = x+1
                self.tw_aw_1.insert(parent='', index='end', iid=x, text='', 
                    values=(
                        x+1,
                        self.df.loc[x,'name'],
                        self.df.loc[x,'password'],
                        self.df.loc[x,'email']
                    )
                )

        else:
            messagebox.showerror("USER NUMBER", "MAXIMUM NUMBER OF USERS REACHED")

    def on_click_del(self):
        selected_user = int(self.tw_aw_1.focus())

        self.df = self.df.drop(selected_user)
        self.df = self.df.reset_index(drop=True)

        # UPDATE TREEVIEW
        self.tw_aw_1.delete(*self.tw_aw_1.get_children())
        for x in range(len(self.df)):
            self.df.loc[x,'index'] = x+1
            self.tw_aw_1.insert(parent='', index='end', iid=x, text='', 
                values=(
                    x+1,
                    self.df.loc[x,'name'],
                    self.df.loc[x,'password'],
                    self.df.loc[x,'email']
                )
            )

        self.df.to_csv('whitelist.csv', index=False)

    def on_click_edit(self):
        AccesWindow.selected_user = int(self.tw_aw_1.focus())
        UserWindow(self)


class UserWindow(tkinter.Toplevel):

    def __init__(self, parent) -> None:
        tkinter.Toplevel.__init__(self, parent)
        user_window_layout(self)

        self.df = pd.read_csv('whitelist.csv', index_col=False)

        self.selected_user_name = self.df.loc[AccesWindow.selected_user,'name']
        self.selected_user_password = self.df.loc[AccesWindow.selected_user,'password']
        self.selected_user_email =self.df.loc[AccesWindow.selected_user,'email']

        self.ent_uw_n.insert(0,self.selected_user_name)
        self.ent_uw_p.insert(0,self.selected_user_password)
        self.ent_uw_e.insert(0,self.selected_user_email)

        self.tw_uw_1.insert(parent='', index='end', iid=AccesWindow.selected_user, text='', 
            values=(
                AccesWindow.selected_user+1,
                self.df.loc[AccesWindow.selected_user,'name'],
                self.df.loc[AccesWindow.selected_user,'password'],
                self.df.loc[AccesWindow.selected_user,'email']
            )
        )
    
    def on_click_save(self):
        user_name = self.ent_uw_n.get()
        user_password = self.ent_uw_p.get()
        user_email = self.ent_uw_e.get()
        
        self.df.loc[AccesWindow.selected_user] = [AccesWindow.selected_user+1, user_name, user_password, user_email]
        self.df.to_csv('whitelist.csv', index=False)

    def on_click_reset(self):
        pass