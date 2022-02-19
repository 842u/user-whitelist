from functions import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from user import User
import tkinter
import csv

class MainWindow(tkinter.Tk):
    version = "0.1.2"
    master_password = "123"
    max_users = 10

    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        main_window_layout(self)

    def on_click(self):
        if  self.ent_mw_1.get() == self.master_password:
            self.withdraw()
            messagebox.showinfo("PASSWORD OK", "ACCES GRANTED")
            self.acces_window = NewWindow(self)
        else:
            messagebox.showerror("PASSWORD CHECK", "WRONG PASSWORD")


class NewWindow(tkinter.Toplevel):
    def __init__(self, parent) -> None:
        tkinter.Toplevel.__init__(self, parent)

        acces_window_layout(self, parent)

        User.instantion_from_whitelist()
        display_user_table(self)

    def on_click(self):
        user_name = self.ent_aw_n.get()
        user_password = self.ent_aw_p.get()
        user_email = self.ent_aw_e.get()
        actual_number_of_users = len(User.user_list)

        if user_name=="" or user_password=="" or user_email=="":
            messagebox.showerror("DATA INCOMPLETE", "PLEASE ENTER ALL DATA")

        elif actual_number_of_users < MainWindow.max_users:
            with open('whitelist.csv', 'a') as f:
                field_names = ['index', 'name', 'password', 'email']
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writerow({
                    'index' : f'{actual_number_of_users+1}', 
                    'name' : f'{user_name}', 
                    'password' : f'{user_password}', 
                    'email' : f'{user_email}'})
            
            User.instantion_from_whitelist()

            add_user_to_table(self)
            
        else:
            messagebox.showerror("USER NUMBER", "MAXIMUM NUMBER OF USERS REACHED")

    def on_click_del(self):
        # x = int(self.tbl.focus())+1
        # self.tbl.delete(x)

        # print(User.user_list)
        # del User.user_list[x]
        # print(User.user_list)

        # ilosc = len(User.user_list)

        # with open('whitelist.csv', 'a') as f:
        #         field_names = ['index', 'name', 'password', 'email']
        #         writer = csv.DictWriter(f, fieldnames=field_names)

        #         for i in range(ilosc):
        #             writer.writerow({
        #                 'index' : f'{i}', 
        #                 'name' : f'{User.user_list[i].name}', 
        #                 'password' : f'{User.user_list[i].password}', 
        #                 'email' : f'{User.user_list[i].email}'})
        pass
            

app_main_window = MainWindow()
app_main_window.mainloop()
