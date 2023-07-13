class Blog:
    def __init__(self, blog_id, title, content, author, publication_date):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.publication_date = publication_date
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
