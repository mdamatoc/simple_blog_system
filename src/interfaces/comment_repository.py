from abc import ABC, abstractmethod

class CommentRepository(ABC):
    @abstractmethod
    def save(self, comment):
        pass

    @abstractmethod
    def get_by_id(self, comment_id):
        pass

    @abstractmethod
    def delete(self, comment):
        pass
