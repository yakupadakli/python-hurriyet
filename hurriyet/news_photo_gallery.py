from datetime import datetime

from hurriyet.client import Client
from hurriyet.models import NewsPhotoGallery as NewsPhotoGalleryModel


class NewsPhotoGallery(Client):
    """Hurriyet news photo gallery operations."""

    def __init__(self, **kwargs):
        super(NewsPhotoGallery, self).__init__(**kwargs)
        self.base_url = "/newsphotogalleries"

    def all(self, news_photo_gallery_id=None, modified_date=None, path=None, top=None, skip=None):
        """
        Get list of news photo galleries.

        :return [NewsPhotoGalleries]: The Hurriyet NewsPhotoGallery.
        """
        filter_data = None
        if news_photo_gallery_id:
            filter_data = "Id eq '%s'" % news_photo_gallery_id

        if modified_date:
            modified_date = datetime.strftime(modified_date, "%Y-%m-%dT%H:%M:%SZ")
            data = "ModifiedDate ge Datetime'%s'" % modified_date
            if filter_data:
                filter_data += ' and %s' % data
            else:
                filter_data = data

        if path:
            data = "Path eq '%s'" % path
            if filter_data:
                filter_data += ' and %s' % data
            else:
                filter_data = data

        params = {"$filter": filter_data, "$top": top, "$skip": skip}
        url = self.base_url
        result = self._get(url, params=params)
        return NewsPhotoGalleryModel.parse_list(result)

    def get(self, news_photo_gallery_id):
        """
        Get a single news photo gallery.

        :return [NewsPhotoGallery]: The Hurriyet NewsPhotoGallery.
        """
        url = "%s/%s" % (self.base_url, news_photo_gallery_id)
        result = self._get(url)
        return NewsPhotoGalleryModel.parse(result)
