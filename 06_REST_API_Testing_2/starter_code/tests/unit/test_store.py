from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('Test store model')

        self.assertEqual(store.name, 'Test store model',
                         "The name of the store after creation does not equal to the constructor argument")

