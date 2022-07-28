#creating widgets
import tkinter as tk
from tkinter import *
from tkinter import ttk

def widgets_create(a):
    root = tk.Tk()
    root.title("Advertising Report")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Overview1')
    tabControl.add(tab2, text='Overview2')
    tabControl.pack(expand=1, fill="both")
    a.to_widgets()
    ttk.Label(tab1,
              text="Overview").grid(column=0,
                                   row=0,
                                   padx=30,
                                   pady=30)
    ttk.Label(tab2,
              text="Variables").grid(column=0,
                                        row=0,
                                        padx=30,
                                        pady=30)

    root.mainloop()