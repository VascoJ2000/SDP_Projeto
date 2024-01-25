from flask import Flask
from Server.controller import Controller


#Business Layer Server
class BusinessLayerServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.controller = Controller()
        self.setup_routes()

    def setup_routes(self):
        # User Routes
        self.app.route('/user/get', methods=['POST'])(self.controller.get_user)
        self.app.route('/user/post', methods=['POST'])(self.controller.add_user)
        self.app.route('/user/put', methods=['POST'])(self.controller.update_user)
        self.app.route('/user/delete', methods=['POST'])(self.controller.delete_user)

        # note Routes
        self.app.route('/note/get', methods=['POST'])(self.controller.get_note)
        self.app.route('/note/post', methods=['POST'])(self.controller.add_note)
        self.app.route('/note/put', methods=['POST'])(self.controller.update_note)
        self.app.route('/note/delete', methods=['POST'])(self.controller.delete_note)