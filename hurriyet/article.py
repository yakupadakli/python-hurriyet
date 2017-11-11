from hurriyet.generic import BaseClient
from hurriyet.models import Article as ArticleModel


class NewsVideo(BaseClient):
    """Hurriyet news video operations."""

    def __init__(self, **kwargs):
        super(NewsVideo, self).__init__(**kwargs)
        self.model_class = ArticleModel
        self.base_url = "/articles"
