import tkinter as tk


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


class LoginPage(tk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        tk.Frame.__init__(self, parent, bg='#C0C0C0')

        # Label + Entry para username
        self.nome_label = tk.Label(self, text="Nome:", font=('Arial', 14), bg='#C0C0C0')
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self, font=('Arial', 14))
        self.nome_entry.pack(pady=5)

        # Label + Entry para password
        self.password_label = tk.Label(self, text="Password:", font=('Arial', 14), bg='#C0C0C0')
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*", font=('Arial', 14))
        self.password_entry.pack(pady=5)

        # Botão de Login
        self.login_button = tk.Button(self, text="Login", font=('Arial', 14), bg='#6d7575', command=self.login)
        self.login_button.pack(pady=10, ipadx=20, ipady=5)

        # Botão de Registo
        self.registo_button = tk.Button(self, text="Registo", font=('Arial', 14), bg='#6d7575', command=self.registo)
        self.registo_button.pack(pady=10, ipadx=20, ipady=5)

    def login(self):
        pass

    def registo(self):
        pass


class UserPage(tk.Frame):
    def __init__(self, parent: tk.Tk) -> None:
        tk.Frame.__init__(self, parent, bg='#C0C0C0')
        pass
