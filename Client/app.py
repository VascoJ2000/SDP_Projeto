from Client.controller import Controller
from dotenv import load_dotenv
import os

load_dotenv()


# Cliente Notlar Application
class Client:
    def __init__(self):
        self.controller = Controller()
        self.controller.client.connect('localhost', os.getenv('BL_LOAD_BALANCER_IP'))

    def run_client(self):
        while True:
            options = input('Enter options: \n l = login \n r = register \n exit = exit \n')
            if options == 'l':
                email = input('Enter your email: ')
                password = input('Enter your password: ')
                self.controller.login(email, password)
            elif options == 'r':
                email = input('Enter your email: ')
                username = input('Chose your username: ')
                password = input('Chose your password: ')
                self.controller.add_user(username=username, email=email, password=password)
            elif options == 'exit':
                print('Exit confirmed. Please close the application')
                break
            else:
                print('Invalid input! Please try again.')
