import mysql.connector


#Data Layer Server
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

    def add_user(self, name, password, email):
        pass

    def add_note(self, user, text):
        pass

    def change_note(self, note_id, new_text):
        pass
