from threading import Thread
from Shared import LoadBalancer
from DB import DLServer
from Server import BLServer
from dotenv import load_dotenv
import os
import time

load_dotenv()


def run_thread(num_bl_servers, num_db_servers):
    # Server List
    server_list = []

    # Load Balancers
    thread1 = Thread(target=LoadBalancer, args=(os.getenv('DB_LOAD_BALANCER_PORT'),))
    thread2 = Thread(target=LoadBalancer, args=(os.getenv('BL_LOAD_BALANCER_PORT'),))

    server_list.append([thread1, thread2])

    thread1.start()
    thread2.start()

    time.sleep(3)

    # Data Layer Servers
    data_layer_list = []
    for i in range(num_db_servers):
        thread = Thread(target=DLServer)
        data_layer_list.append(thread)
        thread.start()
        time.sleep(3)

    server_list.append(data_layer_list)

    # Business Layer Servers
    business_layer_list = []
    for i in range(num_bl_servers):
        thread = Thread(target=BLServer)
        business_layer_list.append(thread)
        thread.start()
        time.sleep(3)

    server_list.append(business_layer_list)

    return server_list
