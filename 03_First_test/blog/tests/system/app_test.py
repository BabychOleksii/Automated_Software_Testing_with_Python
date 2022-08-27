from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('Test blog', 'Test blog Author')
        app.blogs = {'Test blog app': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test blog by Test blog Author (0 posts).')


    def test_aks_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test blog', 'Test blog Author')
            app.ask_create_blog()


    def test_ask_read_blog(self):
        blog = Blog('Test blog', 'Test blog Author')
        app.blogs = {'Test blog': blog}
        with patch('builtins.input', return_value='Test blog'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)


    def test_print_posts(self):
        blog = Blog('Test blog', 'Test blog Author')
        blog.create_post('Test post', 'Test post content')
        app.blogs = {'Test blog': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post test title', 'Post test content')
        expected_print = '''
--- Post test title ---

Post test content

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

