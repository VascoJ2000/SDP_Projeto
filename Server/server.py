import mysql.connector


class Server:
    def __init__(self):
        #Conectar com a base de dados
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="root",
            database="Notlar"
        )

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SHOW DATABASES")

        for x in self.mycursor:
            print(x)
