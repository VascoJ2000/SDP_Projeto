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
        return self.execute_query(query, data)

    def get_entries(self, table, columns, data):
        query = f"SELECT * FROM {table} WHERE ({', '.join(columns)}) IS ({', '.join(['%s'] * len(data))})"
        pass

    def update_entry(self, table, column, new_value, id_column, entry_id):
        query = f"UPDATE {table} SET {column} = %s WHERE {id_column} = %s"
        data = (new_value, entry_id)
        return self.execute_query(query, data)

    def confirm_entry(self, table, column, value):
        query = f"SELECT * FROM {table} WHERE {column} = %s"
        data = (value,)
        if self.mycursor.execute(query, data):
            return self.mycursor.fetchone() is not None
        return False

    def delete_entry(self, table, column, value):
        query = f"DELETE FROM {table} WHERE {column} = %s"
        data = (value,)
        return self.execute_query(query, data)

    def execute_query(self, query, data):
        try:
            self.mycursor.execute(query, data)
            self.mydb.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def disconnect(self):
        self.mycursor.close()
        self.mydb.close()
