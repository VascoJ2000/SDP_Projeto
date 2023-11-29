import DB.app


def db_server_app():
    server = app.DLS("localhost", "3306", "root", "root", "Notlar")
    #server.add_note(1, "hello")
