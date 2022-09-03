from models.item import ItemModel
from models.store import StoreModel

from tests.integration.integration_base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('Test store model')

        self.assertListEqual(store.items.all(), [],
                             "The store's item length was not 0 even though no items were added.")

    def test_crud(self):
        with self.app_context():
            store = StoreModel('Test store model')

            self.assertIsNone(StoreModel.find_by_name('Test store model'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('Test store model'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('Test store model'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('Test store model')
            item = ItemModel('Test item 1', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'Test item 1')

    def test_store_json(self):
        store = StoreModel('Test store model')
        expected = {
            'name': 'Test store model',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('Test store model')
            item = ItemModel('Test item 1', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'Test store model',
                'items': [{'name': 'Test item 1', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)

