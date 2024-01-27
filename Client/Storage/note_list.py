import json
from Client.Storage import Note


class NoteList:
    def __init__(self):
        self.storage = 'Client/Storage/note_list.json'
        self.note_list = self.load_notes()

    def load_notes(self):
        try:
            with open(self.storage, 'r') as file:
                notes = json.load(file)
                return [Note(**note) for note in notes]
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes = [{'Note_id': note.note_id, 'User_id': note.user_id,'Title': note.title, 'Note': note.content} for note in self.note_list]

        with open(self.storage, 'w') as file:
            json.dump(notes, file, indent=2)

    def clear_notes(self):
        with open(self.storage, 'w') as file:
            file.write('[]')

    def add_note(self, note):
        self.note_list.append(note)
        self.save_notes()

    def edit_note(self, note_id, title, content):
        for note in self.note_list:
            if note.note_id == note_id:
                note.title = title
                note.content = content
                return True
        return False

    def get_note_by_id(self, note_id):
        for note in self.note_list:
            if note.note_id == note_id:
                return note
        return None

    def get_note_by_title(self, note_title):
        for note in self.note_list:
            if note.title == note_title:
                return note
        return None

    def get_note_by_user_id(self, user_id):
        user_notes = []
        for note in self.note_list:
            if note.user_id == user_id:
                user_notes.append(note)
        return user_notes

    def delete_note_by_id(self, note_id):
        for note in self.note_list:
            if note.note_id == note_id:
                self.note_list.remove(note)
                self.save_notes()
                return True
        return False

    def delete_note_by_user_id(self, user_id):
        if not self.get_note_by_user_id(user_id):
            return False
        for note in self.note_list:
            if note.user_id == user_id:
                self.note_list.remove(note)
        self.save_notes()
        return True
