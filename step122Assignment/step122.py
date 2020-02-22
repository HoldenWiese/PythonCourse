import tkinter as tk
import step122_gui


class ParentWindow(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        # defining master frame configuration.
        self.master = master
        self.master.minsize(450, 150)
        self.master.title("Check Files")

        # gui widgets!
        step122_gui.load_gui(self)


if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
