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

    def add_entry(self, table, columns, data):
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(data))})"

        self.mycursor.execute(query, data)
        self.mydb.commit()
        return True

    def get_entries(self, table, columns, data):
        query = f"SELECT * FROM {table} WHERE ({', '.join(columns)}) = ({', '.join(['%s'] * len(data))})"

        self.mycursor.execute(query, data)
        result = self.mycursor.fetchall()
        self.mydb.commit()
        return result

    def update_entry(self, table, columns, new_values, id_column, entry_id):
        query = f"UPDATE {table} SET {' = %s, '.join(columns)} = %s WHERE {id_column} = %s"
        data = new_values + (entry_id,)

        self.mycursor.execute(query, data)
        self.mydb.commit()
        return True

    def confirm_entry(self, table, column, value):
        query = f"SELECT * FROM {table} WHERE {column} = %s"
        data = (value,)

        self.mycursor.execute(query, data)
        result = self.mycursor.fetchone() is not None
        self.mydb.commit()
        return result

    def delete_entry(self, table, column, value):
        query = f"DELETE FROM {table} WHERE {column} = %s"
        data = (value,)

        self.mycursor.execute(query, data)
        self.mydb.commit()
        return True

    def disconnect(self):
        self.mycursor.close()
        self.mydb.close()
