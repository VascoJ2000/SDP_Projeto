import json


class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__token = None
        self.__recovery_file = 'Client/Storage/user.json'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_token(self):
        return self.__token

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_token(self, token):
        self.__token = token

    def login(self):
        user_data = [{'User_id': self.__user_id, 'Username': self.__name, 'Email': self.__email, 'Token': self.__token}]

        with open(self.__recovery_file, 'w') as f:
            json.dump(user_data, f, indent=2)

    def logout(self):
        with open(self.__recovery_file, 'w') as f:
            f.write('[]')