from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test blog', 'Test blog Author')

        self.assertEqual('Test blog', b.title)
        self.assertEqual('Test blog Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test blog', 'Test blog Author')
        b2 = Blog('My blog', 'Rolf')

        self.assertEqual(b.__repr__(), 'Test blog by Test blog Author (0 posts).')
        self.assertEqual(b2.__repr__(), 'My blog by Rolf (0 posts).')

    def test_repr_multiple_posts(self):
        b = Blog('Test blog', 'Test blog Author')
        b.posts = ['test']
        b2 = Blog('My blog', 'Rolf')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test blog by Test blog Author (1 post).')
        self.assertEqual(b2.__repr__(), 'My blog by Rolf (2 posts).')



