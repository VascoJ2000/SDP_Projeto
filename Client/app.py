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
        if self.controller.check_status():
            print('It seems that the app was not closed properly and it might not have saved its data properly \n')
            recover = input('Would you like to enter recovery mode? \n * Enter = yes \n * Anything else = no')
            if recover == '':
                self.recovery()
        while True:
            options = input('Options: \n * l = login \n * r = register \n * exit = exit \n')
            if options == 'l':
                email = input('Enter your email: ')
                password = input('Enter your password: ')
                login = self.controller.login(email, password)
                if login[0]:
                    print(login[1])
                    self.logged_in()
                else:
                    print(login[1])
            elif options == 'r':
                email = input('Enter your email: ')
                username = input('Chose your username: ')
                password = input('Chose your password: ')
                result = self.controller.add_user(username=username, email=email, password=password)
                if result[0]:
                    print(result[1])
                else:
                    print(result[1])
            elif options == 'exit':
                print('Exit confirmed. Please close the application')
                break
            else:
                print('Invalid input! Please try again.')

    def logged_in(self):
        print('Logging in...')
        print('Welcome in User')
        self.controller.update_note_list()
        print('Your notes: \n')
        self.controller.display_notes()
        while True:
            option = input('Options: \n'
                           '* add = create a new note \n'
                           '* del = delete a existing note \n'
                           '* put = update a existing note \n'
                           '* get = display notes \n'
                           '* user = user options \n'
                           '* exit = logoff \n')
            if option == 'add':
                self.controller.create_note()
            elif option == 'del':
                try:
                    note_id = int(input('Chose an id from a note that was just displayed to delete it'))
                except ValueError:
                    print('Invalid input! Please try again.')
                else:
                    self.controller.delete_note_by_id(note_id)
            elif option == 'put':
                try:
                    note_id = int(input('Chose an id from a note that was just displayed to start editing it'))
                except ValueError:
                    print('Invalid input! Please try again.')
                else:
                    self.controller.edit_note_by_id(note_id)
            elif option == 'get':
                print('Your notes: \n')
                self.controller.display_notes()
            elif option == 'user':
                self.user_options()
            elif option == 'exit':
                print('Logging off!')
                self.controller.logout()
                break
            else:
                print('Invalid input! Please try again.')

    def user_options(self):
        print('Now in user options')
        while True:
            option = input('Options: \n'
                           '* get = display user info \n'
                           '* put = update user info \n'
                           '* del = delete account \n'
                           '* exit = leave user options \n')
            if option == 'get':
                self.controller.display_user_info()
            elif option == 'put':
                self.controller.edit_user_by_id()
            elif option == 'del':
                print('*****DANGER*****')
                if input('Are you sure you want to PERMANENTLY DELETE your account? (y/n) ') == 'y':
                    self.controller.delete_user()
                    exit()
            elif option == 'exit':
                print('Exiting user options...')
                break
            else:
                print('Invalid input! Please try again.')

    def recovery(self, max_attempts=3):
        print('Entering recovery mode...')
        for i in range(max_attempts):
            email = input('Please enter your email: ')
            if self.controller.recover_state(email):
                print('Email is valid for recovery \n')
                print('Starting check of data integrity...')
                self.controller.recover_data()
                print('Recovery complete')
                break
            else:
                print('Email is not valid for recovery \n')
                print(f'You have {max_attempts-i} attempts left')
        print('Exiting recovery...')
