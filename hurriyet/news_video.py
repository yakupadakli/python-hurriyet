from datetime import datetime

from hurriyet.client import Client
from hurriyet.models import NewsVideo as NewsVideoModel


class NewsVideo(Client):
    """Hurriyet news video operations."""

    def __init__(self, **kwargs):
        super(NewsVideo, self).__init__(**kwargs)
        self.base_url = "/newsvideos"

    def all(self, news_video_id=None, modified_date=None, path=None, top=None, skip=None):
        """
        Get list of news videos.

        :return [NewsVideo]: The Hurriyet NewsVideo.
        """
        filter_data = None
        if news_video_id:
            filter_data = "Id eq '%s'" % news_video_id

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
        return NewsVideoModel.parse_list(result)

    def get(self, news_video_id):
        """
        Get a single news video.

        :return [NewsVideo]: The Hurriyet NewsVideo.
        """
        url = "%s/%s" % (self.base_url, news_video_id)
        result = self._get(url)
        return NewsVideoModel.parse(result)
