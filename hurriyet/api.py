from hurriyet.article import Article
from hurriyet.column import Column


class Api(object):
    """Hurriyet API"""
    ROOT_URL = "https://api.hurriyet.com.tr"
    VERSION = "/v1"

    def __init__(self, api_key, **kwargs):
        """
        Hurriyet Api Instance Constructor

        :param api_key: Api Key
        :param kwargs:
        """
        self.root_url = self.ROOT_URL
        self.version = self.VERSION
        self.base_url = "%s%s" % (self.root_url, self.version)
        self.api_key = api_key

    @property
    def article(self):
        """
        Hurriyet Article Operations

        Available methods:

        all     : All articles.
        get     : Single article.
        """
        return Article(api=self)

    @property
    def column(self):
        """
        Hurriyet Column Operations

        Available methods:

        all     : All columns.
        get     : Single column.
        """
        return Column(api=self)
