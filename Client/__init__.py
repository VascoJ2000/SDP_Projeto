import tkinter as tk
import Client.view

UI = view.view


def clientApp():
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()
