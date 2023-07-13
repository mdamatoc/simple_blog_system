from abc import ABC, abstractmethod

class BlogRepository(ABC):
    @abstractmethod
    def save(self, blog):
        pass

    @abstractmethod
    def get_by_id(self, blog_id):
        pass

    @abstractmethod
    def delete(self, blog):
        pass
