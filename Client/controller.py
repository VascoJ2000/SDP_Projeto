from Shared.client import Client


class Controller:
    def __init__(self):
        self.client = Client()
        self.token = None

    def login(self, email: str, password: str):
        pass

    def logout(self):
        pass

    def register(self, username: str, email: str, password: str):
        pass

    def get_note_list(self):
        pass

    def get_note_by_email(self, email):
        pass

    def get_note_by_id(self, id):
        pass

    def verify_token(self):
        if self.token is None:
            raise Exception("No user is logged in")