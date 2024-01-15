import connection

DLS = connection.DLS("localhost", "3306", "root", "root", "Notlar")


# User methods
def get_user_by_id(user_id):
    DLS.get_entries('notlaruser', 'UserID', user_id)


def get_user_by_email(email):
    DLS.get_entries('notlaruser', 'email', email)


def add_user(username, email, password):
    DLS.add_entry('notlaruser', ("Username", "UserPassword", "Email"), (username, password, email))


def update_user_name(username):
    DLS.update_entry('notlaruser', 'Username', username)


def update_user_email(email):
    DLS.update_entry('notlaruser', 'Email', email)


def update_user_password(password):
    DLS.update_entry('notlaruser', 'UserPassword', password)


def delete_user_by_id(user_id):
    DLS.delete_entry('notlaruser', 'UserID', user_id)


# Note methods
def get_note_by_user_id(user_id):
    DLS.get_entries('usernotes', 'UserID', user_id)


def get_note_by_id(note_id):
    DLS.get_entries('usernotes', 'NoteID', note_id)


def add_note(user_id, title, note):
    DLS.add_entry('usernotes', ("UserID", 'Title', "Note"), (user_id, title, note))


def update_note_content(note_id, new_note):
    DLS.update_entry('usernotes', 'note', new_note, 'NoteID', note_id)


def update_note_title(note_id, new_title):
    DLS.update_entry('usernotes', 'note', new_title, 'NoteID', note_id)


def delete_note_by_id(note_id):
    DLS.delete_entry('usernotes', 'NoteID', note_id)