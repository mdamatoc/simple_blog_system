from src.interfaces.blog_repository import BlogRepository
from src.entities.blog import Blog
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class BlogRepositoryImpl(BlogRepository):
    def __init__(self):
        self.blogs = []

    def save(self, blog: Blog):
        """
        Saves a blog into the blog repository.

        Parameters:
            blog (Blog): Object from Blog class.
        """
        logging.info(f"Saving blog {blog.title}.")
        self.blogs.append(blog)

    def get_by_id(self, blog_id: int) -> Blog or None:
        """
        Looks for a blog by its id.

        Parameters:
            blog_id (int): blog id that will be searched.
        
        Returns:
            If found, Blog object, else, None.
        """
        logging.info(f"Getting blogs by id. Looking for id {blog_id}.")
        for blog in self.blogs:
            if blog.blog_id == blog_id:
                return blog
        return None

    def delete(self, blog: Blog):
        """
        Deletes a blog object.

        Parameters:
            blog (Blog): Blog object that should be deleted.
        """
        logging.warning(f"Deleting blog. Id = {blog.blog_id}")
        if blog in self.blogs:
            self.blogs.remove(blog)
