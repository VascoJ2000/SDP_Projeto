from Shared.client import Client
from Shared.Abstract import BaseController, AuthController
import json

class Controller(BaseController, AuthController):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.token = None
        self.user_id = None

    def get_user(self, user_id, email):
        try:
            self.verify_token()
            res = self.client.get_request('/user', user_id, email)
        except Exception as e:
            return False, str(e)
        else:
            user_id, email, username = res.json()['User_id'], res.json()['Email'], res.json()['Username']
            return True, f'User_id: {user_id},  Email: {email}, Username: {username}'

    def add_user(self, username=None, email=None, password=None):
        try:
            data = {'Username': username, 'Email': email, 'Password': password}
            res = self.client.post_request('/user', data)
            user = res['Username']
        except Exception as e:
            return str(e)
        else:
            return f'User {user} added successfully.'

    def update_user(self, username=None, email=None, password=None):
        try:
            self.verify_token()
            if username:
                data = {'Username': username}
            elif email:
                data = {'Email': email}
            elif password:
                data = {'Password': password}
            else:
                return False, 'No User data was provided'
            res = self.client.update_request('/user', data, token=self.token)
            user = res['Username']
        except Exception as e:
            return str(e)
        else:
            return f'User {user} info updated successfully.'

    def delete_user(self):
        try:
            self.verify_token()
            res = self.client.delete_request('/user', self.user_id, token=self.token)
            user = res['Username']
        except Exception as e:
            return str(e)
        else:
            return f'User {user} was deleted successfully.'

    # Note methods
    def get_note(self, user_id, note_id):
        pass

    def add_note(self):
        pass

    def update_note(self):
        pass

    def delete_note(self):
        pass

    def login(self, email: str, password: str):
        try:
            res = self.client.get_request('/login', email, password)
            self.token = res['token']
            self.user_id = res['User_id']
        except Exception as e:
            return False, str(e)
        else:
            return True, 'User logged in.'

    def token(self):
        try:
            self.verify_token()
            self.client.get_request('/token', None, None, token=self.token)
        except Exception as e:
            return False, str(e)
        else:
            return True, 'User logged in.'

    def logout(self):
        self.token = None

    def verify_token(self):
        if self.token is None:
            raise Exception("No user is logged in")
