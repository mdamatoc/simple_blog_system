import unittest
from src.entities.blog import Blog
from src.infrastructure.blog_repository_impl import BlogRepositoryImpl


class BlogRepositoryImplTests(unittest.TestCase):
    def setUp(self):
        self.blog_repository = BlogRepositoryImpl()

    def test_save_blog(self):
        # Create a blog
        blog_data = {
            'blog_id': 1,
            'title': 'First Blog',
            'content': 'This is the content of the first blog post.',
            'author': 'John Doe',
            'publication_date': '2023-07-12'
        }
        blog = Blog(**blog_data)

        # Save the blog
        self.blog_repository.save(blog)

        # Check if the blog is in the repository
        saved_blog = self.blog_repository.get_by_id(1)
        self.assertEqual(saved_blog, blog)

    def test_get_blog_by_id(self):
        # Create and save a blog
        blog_data = {
            'blog_id': 1,
            'title': 'First Blog',
            'content': 'This is the content of the first blog post.',
            'author': 'John Doe',
            'publication_date': '2023-07-12'
        }
        blog = Blog(**blog_data)
        self.blog_repository.save(blog)

        # Retrieve the blog by ID
        retrieved_blog = self.blog_repository.get_by_id(1)

        # Check if the retrieved blog is the same as the saved blog
        self.assertEqual(retrieved_blog, blog)

    def test_get_nonexistent_blog_by_id(self):
        # Retrieve a non-existent blog by ID
        retrieved_blog = self.blog_repository.get_by_id(1)

        # Check if the retrieved blog is None
        self.assertIsNone(retrieved_blog)

    def test_delete_blog(self):
        # Create and save a blog
        blog_data = {
            'blog_id': 1,
            'title': 'First Blog',
            'content': 'This is the content of the first blog post.',
            'author': 'John Doe',
            'publication_date': '2023-07-12'
        }
        blog = Blog(**blog_data)
        self.blog_repository.save(blog)

        # Delete the blog
        self.blog_repository.delete(blog)

        # Check if the blog is no longer in the repository
        deleted_blog = self.blog_repository.get_by_id(1)
        self.assertIsNone(deleted_blog)


if __name__ == '__main__':
    unittest.main()
