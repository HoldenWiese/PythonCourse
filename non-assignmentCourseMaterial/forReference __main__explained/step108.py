"""
This is an app that opens a window with a First Name and Last name input text box. It includes
a submission button for defining variables with data and a cancel button that closes the app.
"""

# tkinter is the standard GUI library for python. It allows you to make graphical apps.
import tkinter
# This allows you to access tkinter modules using only their name. Ex. Frame instead of tkinter.Frame.
from tkinter import *

# Creating a class
class ParentWindow(Frame):
    # init method means the class takes in a variable(s). These variables are use to instantiate an object.
    # self gives reference to the just created object (i think). master is an attribute passed when creating an object.
    def __init__(self, master):
        # Frame is a container. Master refers to parent window.
        Frame.__init__(self)

        # Initializing object by setting class attribute to instance attribute (i think).
        self.master = master
        # These nex 4 lines are options for the frame widget.
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        # Defining two variables.
        self.varFName = StringVar()
        self.varLName = StringVar()

        # Here we create a label for our first name and last name. self.master refers to parent widget and it is
        # followed by widget options.
        self.lblFName = Label(self.master, text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        # The grid organizes widgets in a table like manner.
        self.lblFName.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.lblLName = Label(self.master, text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30, 0))

        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30, 0), pady=(30, 0))

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0, 0), pady=(30, 0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0, 90), pady=(30, 0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello, {} {}'.format(fn, ln))

    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    # necessary for using tkinter.
    root = Tk()
    # I don't know why this line is necessary.
    App = ParentWindow(root)
    # mainloop() is a method used to run and infinite loop. It makes your program run and checks for interaction.
    root.mainloop()
