# import tkinter
import pandas as pd
from functions import *
from tkinter import *
from tkinter import messagebox

class LoginWindow(Frame):
    __master_password = '123'
    version = '0.3.0'

    def __init__(self, master) -> None:
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        self.login_window_master = master

        login_window_layout(self)

    def on_click_btn_li(self):
        if  self.lw_ent_p.get() == self.__master_password:
            messagebox.showinfo('PASSWORD OK', 'ACCES GRANTED')

            new_toplevel_window = Toplevel(self)
            aw = AccesWindow(new_toplevel_window, self)

        else:
            messagebox.showerror('PASSWORD CHECK', 'WRONG PASSWORD')


class AccesWindow(Frame):
    __user_limit = 10

    def __init__(self, master, login_window):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        self.acces_window_master = master
        self.login_window = login_window

        acces_window_layout(self)

        self.data_frame = pd.read_csv('whitelist.csv', index_col=False)

        update_treeview(treeview=self.aw_tw_1, data=self.data_frame)
        
    def on_click_btn_au(self):
        actual_number_of_users = len(self.data_frame)

        new_user_data = [
            actual_number_of_users+1,
            self.aw_ent_n.get(),
            self.aw_ent_p.get(),
            self.aw_ent_e.get()
        ]

        if self.aw_ent_n.get()=="" or self.aw_ent_p.get()=="" or self.aw_ent_e.get()=="":

            messagebox.showerror("DATA INCOMPLETE", "PLEASE ENTER ALL DATA", parent=self.acces_window_master)

        elif actual_number_of_users < self.__user_limit:

            self.data_frame.loc[-1] = new_user_data

            self.data_frame = self.data_frame.reset_index(drop=True)

            actual_number_of_users = len(self.data_frame)

            self.aw_tw_1.insert(parent='', index='end', iid=actual_number_of_users, text='', 
                values=(
                    self.data_frame.loc[actual_number_of_users-1, 'index'],
                    self.data_frame.loc[actual_number_of_users-1,'name'],
                    self.data_frame.loc[actual_number_of_users-1,'password'],
                    self.data_frame.loc[actual_number_of_users-1,'email']
                )
            )

            update_treeview(treeview=self.aw_tw_1, data=self.data_frame)

            self.data_frame.to_csv('whitelist.csv', index=False)

        else:
            messagebox.showerror("USER NUMBER", "MAXIMUM NUMBER OF USERS REACHED", parent=self.acces_window_master)

    def on_click_btn_du(self):
        self.selected_user = int(self.aw_tw_1.focus())

        self.data_frame = self.data_frame.drop(self.selected_user)
        self.data_frame = self.data_frame.reset_index(drop=True)

        update_treeview(treeview=self.aw_tw_1, data=self.data_frame)

        self.data_frame.to_csv('whitelist.csv', index=False)

    def on_click_btn_eu(self):
        self.selected_user = int(self.aw_tw_1.focus())

        new_toplevel_window = Toplevel(self)
        uw = UserWindow(new_toplevel_window, self)


class UserWindow(Frame):
    def __init__(self, master, acces_window):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=True)

        self.user_window_master = master
        self.acces_window = acces_window

        self.bufored_user_data = self.acces_window.data_frame.loc[self.acces_window.selected_user]

        user_window_layout(self, self.acces_window.selected_user)

        self.uw_tw_1.insert(parent='', index='end', iid=self.acces_window.selected_user, text='', 
                values=(
                    self.acces_window.data_frame.loc[self.acces_window.selected_user, 'index'],
                    self.acces_window.data_frame.loc[self.acces_window.selected_user,'name'],
                    self.acces_window.data_frame.loc[self.acces_window.selected_user,'password'],
                    self.acces_window.data_frame.loc[self.acces_window.selected_user,'email']
                )
            )

    def on_click_btn_s(self):
        edited_user_data = [
            self.acces_window.selected_user+1,
            self.uw_ent_n.get(),
            self.uw_ent_p.get(),
            self.uw_ent_e.get()
        ]

        self.acces_window.data_frame.loc[self.acces_window.selected_user] = edited_user_data

        self.acces_window.data_frame.to_csv('whitelist.csv', index=False)

        self.uw_tw_1.delete(self.acces_window.selected_user)

        self.uw_tw_1.insert(parent='', index='end', iid=self.acces_window.selected_user, text='', values=edited_user_data)

        update_treeview(treeview=self.acces_window.aw_tw_1, data=self.acces_window.data_frame)

    def on_click_btn_r(self):
        self.uw_ent_n.delete(0, 'end')
        self.uw_ent_n.insert(0, self.bufored_user_data[1])

        self.uw_ent_p.delete(0, 'end')
        self.uw_ent_p.insert(0, self.bufored_user_data[2])

        self.uw_ent_e.delete(0, 'end')
        self.uw_ent_e.insert(0, self.bufored_user_data[3])


def main():
    root = Tk()
    lw = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
