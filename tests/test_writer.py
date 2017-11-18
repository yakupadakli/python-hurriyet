import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import Writer


class WriterTest(HurriyetTestCase):

    def test_all(self):
        writers = self.api.writer.all(top=2)
        self.assertIsInstance(writers, list)
        self.assertIsInstance(writers[0], Writer)
        self.assertEqual(len(writers), 2)

    def test_get(self):
        writer = self.api.writer.get("57a8a3430f25441fb419c54a")
        self.assertIsInstance(writer, Writer)


if __name__ == "__main__":
    unittest.main()
