import tkinter as tk
from .LoginPage import *
from .UserPage import *


class view:
    def __init__(self, master) -> None:
        self.master = master

        # Frame
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, width=10000, height=10000, bg='#C0C0C0')
        self.frame.pack()
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Cria a pagina de login.
        self.frames = {}
        self.create_page(LoginPage)
        self.show_page("LoginPage")

    # Mostra a pagina escolhida por nome
    def show_page(self, new_page) -> None:
        page = self.frames[new_page]
        page.tkraise()

    # Cria paginas de acordo com o tipo e atribuilhes um nome para ser possivel navegar entre elas.
    def create_page(self, page_type, *args, **kwargs) -> None:
        #user = kwargs.get("user", Cliente)
        pageName = page_type.__name__
        if page_type == LoginPage:
            page = page_type(parent=self.frame)
        #elif page_type == UserPage:
            #page = page_type(parent=self.frame, controller=self.controller, user=user)
        self.frames[pageName] = page
        page.grid(row=0, column=0, sticky="nsew")
