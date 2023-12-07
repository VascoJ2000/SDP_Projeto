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
        self.execute_query(query, data)

    def change_elem(self, table, column, new_value, id_column, elem_id):
        query = f"UPDATE {table} SET {column} = %s WHERE {id_column} = %s"
        data = (new_value, elem_id)
        self.execute_query(query, data)

    def confirm_entry(self, table, row, value):
        query = f"SELECT * FROM {table} WHERE {row} = %s"
        data = (value,)
        self.mycursor.execute(query, data)
        return self.mycursor.fetchone() is not None

    def delete_entry(self, table, row, value):
        query = f"DELETE FROM {table} WHERE {row} = %s"
        data = (value,)
        self.execute_query(query, data)

    def execute_query(self, query, data):
        self.mycursor.execute(query, data)
        self.mydb.commit()

    def disconnect(self):
        self.mycursor.close()
        self.mydb.close()
