import mysql.connector


#Data Layer Server
#Database = Notlar; Users Table = notlaruser; Notes Table = usernotes;
class DLS:
    def __init__(self, mydb):
        #Conectar com a base de dados
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="Notlar"
        )

        self.mycursor = self.mydb.cursor()

    def add_user(self, username, password, email):
        check = self.mycursor.execute("SELECT EXISTS(SELECT 1 FROM notlaeruser WHERE Username = name VALUE %s)", username)
        if check:
            return False
        query = "INSERT INTO notlaruser (Username, Userpassword, Email) VALUES (%s, $s, $s)"
        data = (username, password, email)
        self.mycursor.execute(query, data)
        self.mydb.commit()
        return True

    def add_note(self, user, text):
        query = "INSERT INTO usernotes (UserID, Note) VALUES (%s, $s)"
        data = (user.get_id(), text)
        self.mycursor.execute(query, data)
        self.mydb.commit()

    def change_note(self, note_id, new_text):
        pass

    def confirm_user(self, name, password):
        return False

    def delete_note(self, note_id):
        pass
