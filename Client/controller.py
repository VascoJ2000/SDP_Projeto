import Client.UI.view as UI
import tkinter as tk


class controller:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.UI = UI.view(self.root)
        self.root.mainloop()
