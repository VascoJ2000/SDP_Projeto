from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self):
        pass

    # User methods
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def update_user_name(self):
        pass

    @abstractmethod
    def update_user_email(self):
        pass

    @abstractmethod
    def update_user_password(self):
        pass

    @abstractmethod
    def delete_user_by_id(self):
        pass

    # Note methods
    @abstractmethod
    def get_note_by_user_id(self, user_id):
        pass

    @abstractmethod
    def get_note_by_id(self, note_id):
        pass

    @abstractmethod
    def add_note(self):
        pass

    @abstractmethod
    def update_note_content(self):
        pass

    @abstractmethod
    def update_note_title(self):
        pass

    @abstractmethod
    def delete_note_by_id(self):
        pass
