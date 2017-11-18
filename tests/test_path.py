import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import Path


class PathTest(HurriyetTestCase):

    def test_all(self):
        paths = self.api.path.all(top=2)
        self.assertIsInstance(paths, list)
        self.assertIsInstance(paths[0], Path)
        self.assertEqual(len(paths), 2)

    def test_get(self):
        path = self.api.path.get("563cddcc67b0a934e44ee2d7")
        self.assertIsInstance(path, Path)


if __name__ == "__main__":
    unittest.main()
