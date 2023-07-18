import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_init_with_id(self):
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_base_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_base_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string([{'id': 1, 'name': 'test'}]), '[{"id": 1, "name": "test"}]')


if __name__ == '__main__':
    unittest.main()
