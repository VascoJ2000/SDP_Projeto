class user:
    def __init__(self, userid, name, password):
        self.id = userid
        self.name = name
        self.password = password
        self.email = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_password(self):
        return self.password

    def set_password(self, new_password):
        self.password = new_password

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email
