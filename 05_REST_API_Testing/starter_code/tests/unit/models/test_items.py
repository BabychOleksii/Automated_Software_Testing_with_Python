from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('Test item 1', 19.99)

        self.assertEqual(item.name, 'Test item 1',
                         'The name of the item after creation does not equal the constructor argument')
        self.assertEqual(item.price, 19.99,
                         'The price of the item after creation does not equal the constructor argument')


    def test_item_json(self):
        item = ItemModel('Test item 1', 19.99)
        expected = {
            'name': 'Test item 1',
            'price': 19.99
        }

        self.assertEqual(item.json(), expected,
                         'TheJSON export of the item is incorrect. '
                         'Received {}, expected {}'.format(item.json(), expected))


