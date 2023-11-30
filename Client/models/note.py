class note:
    def __init__(self, note_id, text):
        self.__id = note_id
        self.__text = text

    def get_id(self):
        return self.__id

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        self.__text = new_text
