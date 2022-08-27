from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test post', 'Test post content')

        self.assertEqual('Test post', p.title)
        self.assertEqual('Test post content', p.content)

    def test_json(self):
        p = Post('Test post', 'Test post content')
        expected = {'title': 'Test post', 'content': 'Test post content'}

        self.assertDictEqual(expected, p.json())



