from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test blog', 'Test blog Author')
        app.blogs = {'Test blog app': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test blog by Test blog Author (0 posts).')

