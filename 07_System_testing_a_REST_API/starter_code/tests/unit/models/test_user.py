from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('Test user', 'testuserpass')

        self.assertEqual(user.username, 'Test user')
        self.assertEqual(user.password, 'testuserpass')

