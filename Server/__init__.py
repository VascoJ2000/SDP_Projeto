from Server.server import BusinessLayerServer
from load_balancer import LoadBalancer
import random
import socket


def run_server():
    pass


def run_load_balancer():
    balancer = LoadBalancer()
    balancer.app.run(debug=True, port=7000)
    return balancer


def get_port(max_attempts=12):
    start_port = 7000
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