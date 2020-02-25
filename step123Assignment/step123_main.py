import tkinter as tk
import tkinter.filedialog
from tkinter import *


class ParentWindow(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(900, 300)
        self.master.title("File Select App")

        def select_file():
            selection = tkinter.filedialog.askdirectory()
            self.my_txt_return = tk.Label(text=selection, width=100)
            self.my_txt_return.grid(row=0, column=1, padx=15, pady=15)

        self.my_btn = tk.Button(text="Select a File", command=select_file)
        self.my_btn.grid(row=0, column=0, padx=15, pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    ParentWindow(root)
    root.mainloop()
