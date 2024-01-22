from DB.server import DataLayerServer
from load_balancer import LoadBalancer
import socket
import random


def run_server():
    new_server = DataLayerServer()
    try:
        server_port = get_port()
        new_server.app.run(debug=True, port=server_port)
    except Exception as e:
        return 'Error: ' + str(e)
    else:
        return new_server


def run_load_balancer():
    balancer = LoadBalancer()
    balancer.app.run(debug=True, port=6000)
    return balancer


def get_port(max_attempts=12):
    start_port = 6000
    for i in range(max_attempts):
        port = random.randint(start_port, start_port+999)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(('localhost', port))
            return port
        except OSError:
            pass
        finally:
            sock.close()
    raise Exception(f"Unable to bind port in {max_attempts} attempts")

