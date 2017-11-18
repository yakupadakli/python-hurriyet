import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import Article


class ArticleTest(HurriyetTestCase):

    def test_all(self):
        articles = self.api.article.all(top=2)
        self.assertIsInstance(articles, list)
        self.assertIsInstance(articles[0], Article)
        self.assertEqual(len(articles), 2)

    def test_get(self):
        article = self.api.article.get("40199111")
        self.assertIsInstance(article, Article)


if __name__ == "__main__":
    unittest.main()
