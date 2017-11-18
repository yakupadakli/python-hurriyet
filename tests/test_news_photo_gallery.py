import unittest

from tests.config import HurriyetTestCase
from hurriyet.models import NewsPhotoGallery


class NewsPhotoGalleryTest(HurriyetTestCase):

    def test_all(self):
        news_photo_galleries = self.api.news_photo_gallery.all(top=2)
        self.assertIsInstance(news_photo_galleries, list)
        self.assertIsInstance(news_photo_galleries[0], NewsPhotoGallery)
        self.assertEqual(len(news_photo_galleries), 2)

    def test_get(self):
        news_photo_gallery = self.api.news_photo_gallery.get("40190642")
        self.assertIsInstance(news_photo_gallery, NewsPhotoGallery)


if __name__ == "__main__":
    unittest.main()
