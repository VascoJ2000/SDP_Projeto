from .Interface.view import *


class Client:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.UI = view(self.root)
        self.root.mainloop()
