from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test blog', 'Test blog Author')
        b.create_post('Test post', 'Test post content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test post')
        self.assertEqual(b.posts[0].content, 'Test post content')

    def test_json_no_posts(self):
        b = Blog('Test blog', 'Test blog Author')
        expected = {'title': 'Test blog', 'author': 'Test blog Author', 'posts': []}

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test blog', 'Test blog Author')
        b.create_post('Test post', 'Test post content')

        expected = {
            'title': 'Test blog',
            'author': 'Test blog Author',
            'posts': [
                {
                    'title': 'Test post',
                    'content': 'Test post content'
                }
            ]
        }

        self.assertDictEqual(expected, b.json())



