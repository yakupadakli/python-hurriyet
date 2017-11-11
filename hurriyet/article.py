from datetime import datetime

from hurriyet.client import Client
from hurriyet.models import Article as ArticleModel


class Article(Client):
    """Hurriyet article operations."""

    def __init__(self, **kwargs):
        super(Article, self).__init__(**kwargs)
        self.base_url = "/articles"

    def all(self, article_id=None, modified_date=None, path=None, top=None, skip=None):
        """
        Get list of articles.

        :return [Articles]: The Hurriyet Articles.
        """
        filter_data = None
        if article_id:
            filter_data = "Id eq '%s'" % article_id

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
        return ArticleModel.parse_list(result)

    def get(self, article_id):
        """
        Get a single article.

        :return [Article]: The Hurriyet Article.
        """
        url = "%s/%s" % (self.base_url, article_id)
        result = self._get(url)
        return ArticleModel.parse(result)
