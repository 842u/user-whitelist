import tkinter
from tkinter import ttk

def window_setup(window_name, title, min_width, min_height, res):

    #   TITLE
    window_name.title(f"{title}")

    #   SIZE
    window_name.min_width = min_width
    window_name.min_height = min_height

    #   RESIZABLE
    if res == False:
        window_name.resizable(0,0)

    #   CENTER
    screen_width = window_name.winfo_screenwidth()
    screen_height = window_name.winfo_screenheight()
    x_coord = int((screen_width/2) - (min_width/2))
    y_coord = int((screen_height/2) - (min_height/2))
    window_name.minsize(window_name.min_width,window_name.min_height)
    window_name.geometry(f"{window_name.min_width}x{window_name.min_height}+{x_coord}+{y_coord}")

def style_setup(window_name, fg, bg):
    
    window_name.style = ttk.Style()
    components = ["TFrame", "TLabel", "TButton"]
    for i in components:
        window_name.style.configure(i, foreground=fg, background=bg)