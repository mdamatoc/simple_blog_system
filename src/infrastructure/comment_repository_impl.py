from src.interfaces.comment_repository import CommentRepository
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class CommentRepositoryImpl(CommentRepository):
    def __init__(self):
        self.comments = []

    def save(self, comment):
        """
        Save a comment.

        Args:
            comment (Comment): The comment to be saved.
        """
        logging.info(f"Saving comment {comment.comment_id} to blog {comment.blog_id}.")
        self.comments.append(comment)

    def get_by_id(self, comment_id):
        """
        Retrieve a comment by its ID.

        Args:
            comment_id (int): The ID of the comment to retrieve.

        Returns:
            Comment: The comment object if found, None otherwise.
        """
        logging.info(f"Retrieving comments by its id. Id = {comment_id}.")
        for comment in self.comments:
            if comment.comment_id == comment_id:
                return comment
        return None

    def delete(self, comment):
        """
        Delete a comment.

        Args:
            comment (Comment): The comment to be deleted.
        """
        logging.warning(f"Deleting comment {comment.comment_id} from blog {comment.blog_id}.")
        if comment in self.comments:
            self.comments.remove(comment)
