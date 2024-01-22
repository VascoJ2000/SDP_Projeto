from flask import Flask, request, jsonify
import hashlib


class LoadBalancer:
    def __init__(self):
        self.app = Flask(__name__)
        self.servers = []
        self.setup_routes()

    def add_server(self):
        try:
            request_data = request.get_json()
            server_ip = request_data['server_ip']
            server_port = request_data['server_port']
            self.servers.append((server_ip, server_port))
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'message': 'Server was added successfully'}), 200

    def get_server(self):
        try:
            ip_client = request.remote_addr
            hashed_ip = self.hash_ip(ip_client)
            server_index = hashed_ip % len(self.servers)
            server = self.servers[server_index]
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        else:
            return jsonify({'Server_ip': server[0], 'Server_port': server[1]}), 200

    def hash_ip(self, ip_address):
        return int(hashlib.md5(ip_address.encode()).hexdigest())

    def setup_routes(self):
        self.app.route('/', methods=['GET'])(self.get_server)
        self.app.route('/', methods=['POST'])(self.add_server)
