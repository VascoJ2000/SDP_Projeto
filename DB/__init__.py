import DB.server


def run_server():
    app = server.DataLayerServer()

    app.app.run(debug=True, port=8888)

