import DB.app


def db_server_app():
    server = app.DLS("localhost", "3306", "root", "root", "Notlar")
    #server.add_note(1, "hi")
    #server.confirm_user("admim", "admim")
    #server.delete_note(3)
    server.change_note(2, "Hello there")
