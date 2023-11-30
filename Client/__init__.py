import tkinter as tk
import Client.view

UI = view.view


def client_app():
    root = tk.Tk()
    ui = UI(root)
    root.mainloop()
