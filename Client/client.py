from Client.UI.view import *
import tkinter as tk


class Client:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.UI = View(self.root)
        self.root.mainloop()
