from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test item 2', 25.99)

            self.assertIsNone(ItemModel.find_by_name('Test item 2'),
                              f"Found an item with name {item.name}, but expected not.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('Test item 2'),
                                 f"Didn't find an item with name {item.name}, but expected.")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Test item 2'),
                              f"Found an item with name {item.name}, but expected not.")
