from tkinter import *
import tkinter as tk
import step122


def load_gui(self):
    self.btn_Browse1 = tk.Button(self.master, text="Browse...", padx=20)
    self.btn_Browse1.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

    self.entry1 = tk.Entry(self.master, width=50)
    self.entry1.grid(row=0, column=1, padx=20, pady=(30, 0), sticky=E)

    self.btn_Browse2 = tk.Button(self.master, text="Browse...", padx=20)
    self.btn_Browse2.grid(row=1, column=0, padx=(20, 10), pady=10)

    self.entry2 = tk.Entry(self.master, width=50)
    self.entry2.grid(row=1, column=1, padx=20, pady=10, sticky=E)

    self.btn_check = tk.Button(text="Check for files...", pady=10)
    self.btn_check.grid(row=2, column=0, padx=(20, 10), pady=(0, 15))

    self.btn_close = tk.Button(text="Close Program", pady=10)
    self.btn_close.grid(row=2, column=1, padx=(20), pady=(0, 15), sticky=E)


if __name__ == "__main__":
    pass
