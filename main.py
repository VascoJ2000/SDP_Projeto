from Client import client_app
from Server import server_app
import DB


if __name__ == '__main__':
    LoadBalancer = DB.run_load_balancer()
    servers = []
    servers.append(DB.run_server())
