from Shared import Client
from Shared.Abstract import BaseController, AuthController
from Client.Storage import User, NoteList, Note
import json


class Controller(BaseController, AuthController):
    def __init__(self):
        super().__init__()
        self.client = Client()
        self.user = None
        self.notes = NoteList()

    # Server connection
    def get_user(self, user_id, email):
        try:
            self.verify_token()
            res = self.client.get_request('/user', user_id, email)
        except Exception as e:
            return False, str(e)
        else:
            user_id, email, username = res.json()['User_id'], res.json()['Email'], res.json()['Username']
            return True, f'User_id: {user_id},  Email: {email}, Username: {username}'

    def add_user(self, username=None, email=None, password=None):
        try:
            data = {
                "Username": username,
                "Email": email,
                "Password": password
            }
            print(type(data))
            self.client.post_request('/user', data)
        except Exception as e:
            return False, str(e)
        else:
            return True, f'User added successfully.'

    def update_user(self, username=None, email=None, password=None):
        try:
            self.verify_token()
            if username:
                data = {'Username': username}
            elif email:
                data = {'Email': email}
            elif password:
                data = {'Password': password}
            else:
                return False, 'No User data was provided'
            self.client.update_request('/user', data, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, f'User info updated successfully.'

    def delete_user(self):
        try:
            self.verify_token()
            data = {'User_id': self.user.get_user_id()}
            self.client.delete_request('/user', data, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, f'User was deleted successfully.'

    # Note methods
    def get_notes(self, user_id=None, note_id=None):
        try:
            self.verify_token()
            res = self.client.get_request('/note', user_id, note_id, token=self.user.get_token())
            data = res['Notes']
        except Exception as e:
            return False, str(e)
        else:

            return True, data

    def add_note(self, user_id=None, title=None, content=None):
        try:
            self.verify_token()
            data = {'User_id': user_id, 'Title': title, 'Note': content}
            self.client.post_request('/note', data, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, f'Note was added successfully.'

    def update_note(self, note_id=None, title=None, content=None):
        try:
            self.verify_token()
            if title and content:
                data = {'Note_id': note_id, 'title': title, 'Note': content}
            else:
                raise Exception('Not enough note data was provided')
            res = self.client.update_request('/note', data, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, f'Note was updated successfully.'

    def delete_note(self, note_id=None):
        try:
            self.verify_token()
            data = {'Note_id': note_id}
            self.client.delete_request('/note', data, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, f'Note was deleted successfully.'

    # Auth
    def login(self, email: str, password: str):
        try:
            res = self.client.get_request('/login', email, password)
            self.user = User(res['User_id'], res['Username'], res['Email'])
            self.user.set_token(res['token'])
            self.user.login()
        except Exception as e:
            return False, str(e)
        else:
            return True, 'User logged in.'

    def token(self):
        try:
            self.verify_token()
            self.client.get_request('/token', None, None, token=self.user.get_token())
        except Exception as e:
            return False, str(e)
        else:
            return True, 'User logged in.'

    def logout(self):
        self.notes.delete_note_by_user_id(self.user.get_user_id())
        self.user.logout()
        self.user = None

    def verify_token(self):
        if self.user.get_token() is None:
            raise Exception("No user is logged in")

    # Client side operations
    def update_note_list(self):
        result = self.get_notes(self.user.get_user_id())
        if result[0]:
            self.notes.delete_note_by_user_id(self.user.get_user_id())
            notes = result[1]
            for note in notes:
                new_note = Note(note_id=note[0], user_id=note[1], title=note[2], content=note[3])
                self.notes.add_note(new_note)

    def display_notes(self):
        notes = self.notes.get_note_by_user_id(self.user.get_user_id())
        for n in notes:
            print(f'Note_id: {n.note_id} - Title: {n.title}')

    def display_note_by_id(self, note_id):
        n = self.notes.get_note_by_id(note_id)
        print(f'Title: {n.title}')
        return n

    def display_note_by_title(self, title):
        n = self.notes.get_note_by_title(title)
        print(f'Title: {n.title}')
        return n

    def edit_note_by_id(self, note_id):
        n = self.notes.get_note_by_id(note_id)
        print('Change content or press enter to keep the same: \n')
        content = input(f'{n.title}: {n.content}\n')
        if content == '':
            content = n.content
        print('Choose a new title or press enter to keep the same: \n')
        title = input('Title: ' + n.title)
        if title == '':
            title = n.title
        if self.notes.edit_note(note_id, title, content):
            result = self.notes.edit_note(note_id, title, content)
            if result[0]:
                print(result[1])
            else:
                print('Note was updated locally but was not in database')
        else:
            print('Note was note able to be updated')

    def create_note(self):
        content = input('Write a new note: \n')
        while content == '':
            content = input('Note content cannot be blank \n')
        title = input('Give the note a title \n')
        while title == '':
            title = input('Note title cannot be blank \n')
        n = Note(None, self.user.get_user_id(), title, content)
        self.notes.add_note(n)
        result = self.add_note(n.user_id, n.title, n.content)
        if result[0]:
            print(result[1])
        else:
            print('Note was not able to be added to database but is saved')

    def delete_note_by_id(self, note_id):
        if self.notes.delete_note_by_id(note_id):
            result = self.notes.delete_note_by_id(note_id)
            if result[0]:
                print(result[1])
            else:
                print('Note was deleted but was not able to be removed from database')
        else:
            print('Note was note able to be deleted')

    # Recovery
    def check_status(self):
        with open('Client/Storage/user.json') as user_file:
            user_data = user_file.read()
            if user_data.strip() == '' or user_data.strip() == '[]':
                return False
            else:
                return True

    def recover_state(self, email):
        with open('Client/Storage/user.json') as user_file:
            user_data = user_file.read()
            for user in json.loads(user_data):
                if user['email'] == email:
                    self.user = User(user['User_id'], user['username'], user['email'])
                    self.user.set_token(user['Token'])
                    return True
            return False

    def recover_data(self):
        user_id = self.user.get_user_id()
        db_notes = self.get_notes(user_id, None)[1]
        notes = self.notes.get_note_by_user_id(user_id)
        if input('Do you want to remove database notes not present in local storage? (y/n): \n') == 'y':
            print('Removing notes...')
            for note in db_notes:
                if note[0] not in notes:
                    self.delete_note(note[0])
            db_notes = self.get_notes(user_id, None)[1]
        if input('Do you want to add notes not present in database? (y/n): \n') == 'y':
            print('Adding notes...')
            for note in notes:
                if note['Note_id'] is None:
                    self.add_note(user_id=user_id, title=note['Title'], content=note['Note'])
            db_notes = self.get_notes(user_id, None)[1]
        if input('Do you want to update notes in database? (y/n): \n') == 'y':
            print('Update notes...')
            count = 0
            for note in notes:
                for db_note in db_notes:
                    if note['Note_id'] == db_note[0]:
                        title = None
                        content = None
                        if note['Title'] != db_note[2]:
                            title = note['Title']
                        if note['Content'] != db_note[3]:
                            content = note['Content']
                        try:
                            self.update_note(user_id, title=title, content=content)
                        except Exception as e:
                            pass
                        else:
                            count += 1
            print(f'Updated {count} notes')
        print('Normalizing data...')
        self.update_note_list()
