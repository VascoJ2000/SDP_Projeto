from flask import Flask, request
from DB.controller import Controller


class DataLayerServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.controller = Controller()
        self.setup_routes()

    def setup_routes(self):
        # User Routes
        self.app.route('/user/id/<user_id>', methods=['GET'])(self.controller.get_user_by_id)
        self.app.route('/user/email/<email>', methods=['GET'])(self.controller.get_user_by_email)
        self.app.route('/user', methods=['POST'])(self.controller.add_user)
        self.app.route('/user/name', methods=['PUT'])(self.controller.update_user_name)
        self.app.route('/user/email', methods=['PUT'])(self.controller.update_user_email)
        self.app.route('/user/password', methods=['PUT'])(self.controller.update_user_password)
        self.app.route('/user/id', methods=['DELETE'])(self.controller.delete_user_by_id)

        #Note Routes
        self.app.route('/note/user_id/<user_id>', methods=['GET'])(self.controller.get_note_by_user_id)
        self.app.route('/note/id/<note_id>', methods=['GET'])(self.controller.get_note_by_id)
        self.app.route('/note', methods=['POST'])(self.controller.add_note)
        self.app.route('/note', methods=['PUT'])(self.controller.update_note_content)
        self.app.route('/note/title', methods=['PUT'])(self.controller.update_note_title)
        self.app.route('/note', methods=['DELETE'])(self.controller.delete_note_by_id)