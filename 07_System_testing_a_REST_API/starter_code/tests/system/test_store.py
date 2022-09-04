from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/TestStore')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('TestStore'))
                self.assertDictEqual(d1={'name': 'TestStore', 'items': []},
                                     d2=json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/TestStore2')
                response = client.post('/store/TestStore2')

                self.assertEqual(response.status_code, 400)
                
    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('TestStore3').save_to_db()
                response = client.delete('/store/TestStore3')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'message': 'Store deleted.'},
                                     d2=json.loads(response.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('TestStore4').save_to_db()
                response = client.get('/store/TestStore4')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'name': 'TestStore4', 'items': []},
                                     d2=json.loads(response.data))

    def test_store_not_found(self):
        with self.app() as client:
            response = client.get('/store/TestStore5')
            self.assertEqual(response.status_code, 404)
            self.assertDictEqual({'message': 'Store not found.'},
                                 json.loads(response.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('TestStore6').save_to_db()
                ItemModel('TestItem', 22.99, 1).save_to_db()
                response = client.get('/store/TestStore6')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'name': 'TestStore6', 'items': [{'name': 'TestItem', 'price': 22.99}]},
                                     d2=json.loads(response.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('TestStore7').save_to_db()
                response = client.get('/stores')

                self.assertDictEqual(d1={'stores': [{'name': 'TestStore7', 'items': []}]},
                                     d2=json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('TestStore8').save_to_db()
                ItemModel('TestItem2', 27.99, 1).save_to_db()

                response = client.get('/stores')
                self.assertDictEqual(d1={'stores': [{'name': 'TestStore8',
                                                     'items': [{'name': 'TestItem2', 'price': 27.99}]}]},
                                     d2=json.loads(response.data))
