import unittest
from src.entities.comment import Comment
from src.infrastructure.comment_repository_impl import CommentRepositoryImpl



class CommentRepositoryImplTests(unittest.TestCase):
    def setUp(self):
        self.comment_repository = CommentRepositoryImpl()

    def test_save_comment(self):
        # Create a comment
        comment_data = {
            'comment_id': 1,
            'content': 'Great blog!',
            'author': 'Alice',
            'publication_date': '2023-07-12',
            'blog_id': 1
        }
        comment = Comment(**comment_data)

        self.comment_repository.save(comment)

        # Check if the comment is in the repository
        saved_comment = self.comment_repository.get_by_id(1)
        self.assertEqual(saved_comment, comment)

    def test_get_comment_by_id(self):
        # Create and save a comment
        comment_data = {
            'comment_id': 1,
            'content': 'Great blog!',
            'author': 'Alice',
            'publication_date': '2023-07-12',
            'blog_id': 1
        }
        comment = Comment(**comment_data)
        self.comment_repository.save(comment)

        # Retrieve the comment by ID
        retrieved_comment = self.comment_repository.get_by_id(1)

        # Check if the retrieved comment is the same as the saved comment
        self.assertEqual(retrieved_comment, comment)

    def test_get_nonexistent_comment_by_id(self):
        # Retrieve a non-existent comment by ID
        retrieved_comment = self.comment_repository.get_by_id(1)

        # Check if the retrieved comment is None
        self.assertIsNone(retrieved_comment)

    def test_delete_comment(self):
        # Create and save a comment
        comment_data = {
            'comment_id': 1,
            'content': 'Great blog!',
            'author': 'Alice',
            'publication_date': '2023-07-12',
            'blog_id': 1
        }
        comment = Comment(**comment_data)
        self.comment_repository.save(comment)

        # Delete the comment
        self.comment_repository.delete(comment)

        # Check if the comment is no longer in the repository
        deleted_comment = self.comment_repository.get_by_id(1)
        self.assertIsNone(deleted_comment)


if __name__ == '__main__':
    unittest.main()
