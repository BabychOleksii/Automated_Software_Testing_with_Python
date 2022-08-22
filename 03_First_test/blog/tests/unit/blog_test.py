from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test blog", "Test blog Author")

        self.assertEqual("Test blog", b.title)
        self.assertEqual("Test blog Author", b.author)
        self.assertListEqual([], b.posts)

