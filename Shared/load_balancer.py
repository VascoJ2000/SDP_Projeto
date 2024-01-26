from flask import Flask, request, jsonify
import hashlib


class LoadBalancer:
    def __init__(self, port):
        self.app = Flask(__name__)
        self.servers = []
        self.setup_routes()
        self.run_app(port)

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
        if len(self.servers) == 0:
            return '', 425
        try:
            ip_client = request.remote_addr
            server = self.hash_ip(ip_client)
        except Exception as e:
            return jsonify({'error': str(e)}), 406
        else:
            return jsonify({'Server_ip': server[0], 'Server_port': server[1]}), 200

    def hash_ip(self, ip_address):
        hashed_ip = int(hashlib.md5(ip_address.encode()).hexdigest())
        server_index = hashed_ip % len(self.servers)
        return self.servers[server_index]

    def setup_routes(self):
        self.app.route('/', methods=['GET'])(self.get_server)
        self.app.route('/', methods=['POST'])(self.add_server)

    def run_app(self, port):
        self.app.run(port=port)
        print(f'Load Balancer running on port {port}')
