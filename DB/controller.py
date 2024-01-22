import DB.db as db
from flask import Flask, request, jsonify

app = Flask(__name__)


class Controller:
    def __init__(self):
        self.db = db.DLS("localhost", "3306", "root", "root", "notlar")

    # User methods
    @app.route('/user/id', methods=['GET'])
    def get_user_by_id(self, user_id):
        try:
            user = self.db.get_entries('notlaruser', ('ID',), (user_id,))
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            return jsonify({
                'User_id': user[0][0],
                'Email': user[0][1],
                'Username': user[0][2],
                'Password': user[0][3]
            }), 200

    @app.route('/user/email', methods=['GET'])
    def get_user_by_email(self, email):
        try:
            user = self.db.get_entries('notlaruser', ('Email',), (email,))
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if len(user) > 0:
                return jsonify({
                    'User_id': user[0][0],
                    'Email': user[0][1],
                    'Username': user[0][2],
                    'Password': user[0][3]
                }), 200
            else:
                return jsonify({'message': 'User not found'}), 404

    @app.route('/user', methods=['POST'])
    def add_user(self, username, email, password):
        try:
            data = self.db.add_entry('notlaruser', ("Username", "UserPassword", "Email"), (username, password, email))
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if data:
                return jsonify({'message': 'User added successfully'}), 200
            else:
                return jsonify({'message': 'User was not added'}), 300
    @app.route('/user/name', methods=['PUT'])
    def update_user_name(self, username):
        try:
            data = self.db.update_entry('notlaruser', 'Username', username)
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if data:
                return jsonify({'message': 'Username was updated successfully'}), 200
            else:
                return jsonify({'message': 'Username was not updated'}), 300

    @app.route('/user/email', methods=['PUT'])
    def update_user_email(self, email):
        try:
            data = self.db.update_entry('notlaruser', 'Email', email)
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if data:
                return jsonify({'message': 'User email was updated successfully'}), 200
            else:
                return jsonify({'message': 'User email was not updated'}), 300

    @app.route('/user/password', methods=['PUT'])
    def update_user_password(self, password):
        try:
            data = self.db.update_entry('notlaruser', 'UserPassword', password)
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if data:
                return jsonify({'message': 'User password was updated successfully'}), 200
            else:
                return jsonify({'message': 'User password was not updated'}), 300

    @app.route('/user/id', methods=['DELETE'])
    def delete_user_by_id(self, user_id):
        try:
            data = self.db.delete_entry('notlaruser', 'ID', user_id)
        except Exception as e:
            return jsonify('Error: ' + str(e)), 500
        else:
            if data:
                return jsonify({'message': 'User deleted successfully'}), 200
            else:
                return jsonify({'message': 'User was not deleted'}), 300

    # Note methods
    def get_note_by_user_id(self, user_id):
        self.db.get_entries('usernotes', 'ID', user_id)

    def get_note_by_id(self, note_id):
        self.db.get_entries('usernotes', 'ID', note_id)

    def add_note(self, user_id, title, note):
        self.db.add_entry('usernotes', ("UserID", 'Title', "Note"), (user_id, title, note))

    def update_note_content(self, note_id, new_note):
        self.db.update_entry('usernotes', 'note', new_note, 'NoteID', note_id)

    def update_note_title(self, note_id, new_title):
        self.db.update_entry('usernotes', 'note', new_title, 'NoteID', note_id)

    def delete_note_by_id(self, note_id):
        self.db.delete_entry('usernotes', 'NoteID', note_id)
