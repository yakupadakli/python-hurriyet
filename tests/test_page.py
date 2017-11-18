import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import Page


class PageTest(HurriyetTestCase):

    def test_all(self):
        pages = self.api.page.all(top=2)
        self.assertIsInstance(pages, list)
        self.assertIsInstance(pages[0], Page)
        self.assertEqual(len(pages), 2)

    def test_get(self):
        page = self.api.page.get("571637076d774a1b64c18b2d")
        self.assertIsInstance(page, Page)


if __name__ == "__main__":
    unittest.main()
