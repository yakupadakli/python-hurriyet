import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import Column


class ColumnTest(HurriyetTestCase):

    def test_all(self):
        columns = self.api.column.all(top=2)
        self.assertIsInstance(columns, list)
        self.assertIsInstance(columns[0], Column)
        self.assertEqual(len(columns), 2)

    def test_get(self):
        column = self.api.column.get("40190106")
        self.assertIsInstance(column, Column)


if __name__ == "__main__":
    unittest.main()
