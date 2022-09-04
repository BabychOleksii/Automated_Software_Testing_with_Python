from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('Test user 2', 'testuser2pass')

            self.assertIsNone(UserModel.find_by_username('Test user 2'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('Test user 2'))
            self.assertIsNotNone(UserModel.find_by_id(1))


