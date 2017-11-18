import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import NewsVideo


class NewsVideoTest(HurriyetTestCase):

    def test_all(self):
        news_videos = self.api.news_video.all(top=2)
        self.assertIsInstance(news_videos, list)
        self.assertIsInstance(news_videos[0], NewsVideo)
        self.assertEqual(len(news_videos), 2)

    def test_get(self):
        news_video = self.api.news_video.get("40393187")
        self.assertIsInstance(news_video, NewsVideo)


if __name__ == "__main__":
    unittest.main()
