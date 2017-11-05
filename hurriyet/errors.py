import six


class HurriyetError(Exception):
    message = six.text_type("Unknown error")

    def __init__(self, message=None, status=None):
        self.message = six.text_type(message) if message else self.message
        self.status = status
        super(HurriyetError, self).__init__(message, status)

    def __str__(self):
        return self.message


class ConnectionError(HurriyetError):
    pass


class NotFound(HurriyetError):
    message = six.text_type(u"Not Found")


class ArticleNotFound(NotFound):
    message = six.text_type(u"Article Not Found")
