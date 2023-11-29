class note:
    def __init__(self, note_id, text):
        self.id = note_id
        self.text = text

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def set_text(self, new_text):
        self.text = new_text
