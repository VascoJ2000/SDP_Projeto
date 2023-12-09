import DB.app


def db_server_app():
    server = app.DLS("localhost", "3306", "root", "root", "Notlar")
    #server.add_entry("notlaruser", ("Username", "UserPassword", "Email"),("Vasco João", "123456789", "30005819@students.ual.pt"))
    #server.add_entry("usernotes", ("UserID", "Note"), (2, "Hello there"))
    #server.change_elem("usernotes", "Note", "Hi","ID", "2")
    #print(server.confirm_entry("usernotes", "Note", "Hi"))
    #server.delete_entry("usernotes", "Note", "Hello there")
