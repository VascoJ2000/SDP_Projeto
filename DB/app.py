import mysql.connector


#Data Layer Server
#Database = Notlar; Users Table = notlaruser; Notes Table = usernotes;
class DLS:
    def __init__(self, host, port, user, password, database):
        #Conectar com a base de dados
        self.mydb = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        self.mycursor = self.mydb.cursor()

    def add_user(self, username, password, email):
        query = "INSERT INTO notlaruser (Username, Userpassword, Email) VALUES (%s, %s, %s)"
        data = (username, password, email)
        self.mycursor.execute(query, data)
        self.mydb.commit()

    def add_note(self, user_id, text):
        query = "INSERT INTO usernotes (UserID, Note) VALUES (%s, %s)"
        data = (user_id, text)
        self.mycursor.execute(query, data)
        self.mydb.commit()

    def change_note(self, note_id, new_text):
        pass

    def confirm_user(self, username, password):
        query = "SELECT EXISTS(SELECT 1 FROM notlaeruser WHERE Username = name VALUE %s)"
        check = self.mycursor.execute(query, username)
        if check:
            return True
        return False

    def delete_note(self, note_id):
        pass
