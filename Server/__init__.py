import mysql.connector


def serverApp():
    # Conectar com a base de dados
    mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="Notlar"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)
