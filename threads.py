from threading import Thread
from load_balancer import LoadBalancer
from DB import DLServer
from Server import BLServer
from dotenv import load_dotenv
import os

load_dotenv()


def run_thread(num_bl_servers, num_db_servers):
    # Load Balancers
    thread1 = Thread(target=LoadBalancer, args=(os.getenv('DB_LOAD_BALANCER_IP'),))
    thread2 = Thread(target=LoadBalancer, args=(os.getenv('BL_LOAD_BALANCER_IP'),))

    thread1.start()
    thread2.start()

    # Data Layer Servers
    for i in range(num_db_servers):
        thread = Thread(target=DLServer)
        thread.start()

    # Business Layer Servers
    for i in range(num_bl_servers):
        thread = Thread(target=BLServer)
        thread.start()
