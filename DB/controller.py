from DB.db import DLS
from Shared.Abstract import BaseController
from flask import request, jsonify


class Controller(BaseController):
    def __init__(self):
        super().__init__()
        self.db = DLS("localhost", "3306", "root", "root", "notlar")

    # User methods
    def get_user(self, user_id, email):
        try:
            if user_id != 'None':
                user = self.db.get_entries('notlaruser', ('ID',), (user_id,))
            elif email != 'None':
                user = self.db.get_entries('notlaruser', ('Email',), (email,))
            else:
                raise Exception('No User data found in request')

            if len(user) == 0:
                raise Exception('No such user found')
            data = {
                "User_id": user[0][0],
                "Email": user[0][3],
                "Username": user[0][1],
                "Password": user[0][2]
            }
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            return jsonify(data), 200

    def add_user(self):
        try:
            request_data = request.get_json()
            username = request_data['Username']
            password = request_data['Password']
            email = request_data['Email']
            data = self.db.add_entry('notlaruser', ("Username", "UserPassword", "Email"), (username, password, email))
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'User added successfully'}), 200
            else:
                return jsonify({'message': 'User was not added'}), 300

    def update_user(self):
        try:
            request_data = request.get_json()
            user_id = request_data['User_id']

            username = request_data['Username']
            email = request_data['Email']
            password = request_data['Password']
            data = self.db.update_entry('notlaruser', ('Username', 'Email', 'UserPassword'), (username, email, password), 'ID', user_id)
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'User was updated successfully'}), 200
            return jsonify({'message': 'User was not updated'}), 300

    def delete_user(self):
        try:
            request_data = request.get_json()
            user_id = request_data.get('User_id')
            data = self.db.delete_entry('notlaruser', 'ID', user_id)
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'User deleted successfully'}), 200
            else:
                return jsonify({'message': 'User was not deleted'}), 300

    # Note methods
    def get_notes(self, user_id, note_id=None):
        try:
            if user_id:
                data = self.db.get_entries('usernotes', 'UserID', user_id)
            elif note_id:
                data = self.db.get_entries('usernotes', 'ID', note_id)
            else:
                raise Exception('No data found in request')
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'Notes': data}), 200
            else:
                return jsonify({'message': 'No notes were found'}), 404

    def add_note(self):
        try:
            request_data = request.get_json()
            user_id = request_data.get('User_id')
            title = request_data.get('Title')
            note = request_data.get('Note')
            data = self.db.add_entry('usernotes', ("UserID", 'Title', "Note"), (user_id, title, note))
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'New Note successfully added'}), 200
            else:
                return jsonify({'message': 'New Note was not added'}), 300

    def update_note(self):
        try:
            request_data = request.get_json()
            note_id = request_data.get('Note_id')
            new_note = request_data.get('Note')
            new_title = request_data.get('Title')
            data = self.db.update_entry('usernotes', ('Title', 'Note'), (new_title, new_note), 'NoteID', note_id)
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'Note content successfully updated'}), 200
            else:
                return jsonify({'message': 'Note content was not updated'}), 300

    def delete_note(self):
        try:
            request_data = request.get_json()
            note_id = request_data.get('Note_id')
            data = self.db.delete_entry('usernotes', 'NoteID', note_id)
        except Exception as e:
            return jsonify({'Error':  str(e)}), 500
        else:
            if data:
                return jsonify({'message': 'Note successfully deleted'}), 200
            else:
                return jsonify({'message': 'Note was not deleted'}), 300
