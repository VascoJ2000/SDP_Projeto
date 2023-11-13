import tkinter as tk


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
