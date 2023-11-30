class user:
    def __init__(self, userid, username, password):
        self.__id = userid
        self.__name = username
        self.__password = password
        self.__email = None

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, new_username):
        self.__name = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email
