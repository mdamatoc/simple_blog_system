from src.entities.blog import Blog
from src.entities.comment import Comment
from src.infrastructure.blog_repository_impl import BlogRepositoryImpl
from src.infrastructure.comment_repository_impl import CommentRepositoryImpl


def create_populated_usecases():
    """
    Create and populate use cases for demonstration.

    Returns:
        BlogRepositoryImpl: The blog repository with populated data.
    """

    # Create repositories
    blog_repository = BlogRepositoryImpl()
    comment_repository = CommentRepositoryImpl()

    # Create a new blog
    blog_data = {
        'blog_id': 1,
        'title': 'First Blog',
        'content': 'This is the content of the first blog post.',
        'author': 'John Doe',
        'publication_date': '2023-07-12'
    }
    my_first_blog = Blog(**blog_data)
    blog_repository.save(my_first_blog)

    # Create comment 1
    comment_data1 = {
        'comment_id': 1,
        'content': 'Great blog!',
        'author': 'Alice',
        'publication_date': '2023-07-12',
        'blog_id': 1  # Associate comment with blog_id 1
    }
    comment1 = Comment(**comment_data1)
    comment_repository.save(comment1)
    my_first_blog.add_comment(comment1)

    # Create comment 2
    comment_data2 = {
        'comment_id': 2,
        'content': 'Nice post!',
        'author': 'Bob',
        'publication_date': '2023-07-12',
        'blog_id': 1  # Associate comment with blog_id 1
    }
    comment2 = Comment(**comment_data2)
    comment_repository.save(comment2)
    my_first_blog.add_comment(comment2)

    return blog_repository


if __name__ == "__main__":
    # Call a function to create and populated some usecases to be shown.
    blog_repository = create_populated_usecases()

    # Retrieve the created blog and its comments
    my_first_blog = blog_repository.get_by_id(1)

    if my_first_blog:
        print(f"Blog: {my_first_blog.title}")
        print("Comments:")
        for comment in my_first_blog.comments:
            if comment:
                print(f"- {comment.content} by {comment.author}")
            else:
                print("- Comment not found")
    else:
        print("Blog not found")
