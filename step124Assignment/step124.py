# imports
import tkinter
from tkinter import *
import tkinter.filedialog
import os
import time
import sqlite3
import shutil

# Creating my database
conn = sqlite3.connect('db_124.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles\
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_fileName TEXT, \
                col_timeStamp TEXT \
                )")


# My Functions

def pickSourceDir(**kwargs):
    myDir = tkinter.filedialog.askdirectory()
    source_dir.delete(0, END)
    source_dir.insert(0, myDir)


def pickDestDir():
    myDir = tkinter.filedialog.askdirectory()
    destination_dir.delete(0, END)
    destination_dir.insert(0, myDir)


def moveFiles():
    source_entry = source_dir.get()
    destination = destination_dir.get()
    source_files = os.listdir(source_entry)
    for x in source_files:
        if x.endswith(".txt"):
            full = os.path.join(source_entry, x)
            epochTime = os.path.getmtime(full)
            localTime = str(time.ctime(epochTime))
            phrase = "\n" + x + " was last modified " + localTime + "."
            with conn:
                cur.execute("INSERT INTO tbl_txtFiles (col_fileName, col_timeStamp) VALUES (?, ?)", (x, localTime,))
                conn.commit()
            print(phrase)
            shutil.move(full, destination)


# My tkinter GUI

m = tkinter.Tk()

m.minsize(750, 150)
m.title("Check Files")

btn_Browse1 = Button(m, text="Browse...", padx=20, command=pickSourceDir)
btn_Browse1.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

source_dir = Entry(m, width=100)
source_dir.grid(row=0, column=1, padx=20, pady=(30, 0), sticky=E)

btn_Browse2 = Button(m, text="Browse...", padx=20, command=pickDestDir)
btn_Browse2.grid(row=1, column=0, padx=(20, 10), pady=10)

destination_dir = Entry(m, width=100)
destination_dir.grid(row=1, column=1, padx=20, pady=10, sticky=E)

btn_check = Button(text="Check for files...", pady=10, command=moveFiles)
btn_check.grid(row=2, column=0, padx=(20, 10), pady=(0, 15))

btn_close = Button(text="Close Program", pady=10, command=m.destroy)
btn_close.grid(row=2, column=1, padx=20, pady=(0, 15), sticky=E)

m.mainloop()
