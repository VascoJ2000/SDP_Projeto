from Client import client_app
from Server import server_app
import DB.db
from load_balancer import LoadBalancer


if __name__ == '__main__':
    DB.run_server()
