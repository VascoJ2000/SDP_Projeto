from Server.controller import Controller
from Shared.Abstract.server import Server
import os


# Business Layer Server
class BusinessLayerServer(Server):
    def __init__(self):
        self.controller = Controller()
        super().__init__()
        self.connect_to_balancer('localhost', os.getenv('BL_LOAD_BALANCER_IP'))
        self.controller.client.connect('localhost', os.getenv('DB_LOAD_BALANCER_IP'))
        self.run_server()

    def setup_routes(self):
        # User Routes
        self.app.route('/user/<user_id>&<email>', methods=['GET'])(self.controller.get_user)
        self.app.route('/user', methods=['POST'])(self.controller.add_user)
        self.app.route('/user', methods=['PUT'])(self.controller.update_user)
        self.app.route('/user', methods=['DELETE'])(self.controller.delete_user)

        # note Routes
        self.app.route('/note', methods=['GET'])(self.controller.get_notes)
        self.app.route('/note', methods=['POST'])(self.controller.add_note)
        self.app.route('/note', methods=['PUT'])(self.controller.update_note)
        self.app.route('/note', methods=['DELETE'])(self.controller.delete_note)

        # Authentication
        self.app.route('/login/<email>&<password>', methods=['GET'])(self.controller.login)
        self.app.route('/token', methods=['GET'])(self.controller.token)
