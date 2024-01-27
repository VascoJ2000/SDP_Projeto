from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self):
        pass

    # User methods
    @abstractmethod
    def get_user(self, user_id, email):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def update_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    # Note methods
    @abstractmethod
    def get_note(self, user_id, note_id):
        pass

    @abstractmethod
    def add_note(self):
        pass

    @abstractmethod
    def update_note(self):
        pass

    @abstractmethod
    def delete_note(self):
        pass
