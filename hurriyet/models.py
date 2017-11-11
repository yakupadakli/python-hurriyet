from hurriyet import errors


class ResultSet(list):
    """A list like object that holds results from a Hurriyet API query."""


class Model(object):
    _not_found_error_class = errors.NotFound

    def __init__(self, **kwargs):
        self._repr_values = ["id"]

    @classmethod
    def parse(cls, data, sub_item=False):
        data = data or {}
        if not data and not sub_item:
            raise cls._not_found_error_class()
        instance = cls() if data else None
        for key, value in data.items():
            if type(value) == str:
                value = value.strip()
            setattr(instance, key.lower(), value)
        return instance

    @classmethod
    def parse_list(cls, data):
        """Parse a list of JSON objects into a result set of model instances."""
        results = ResultSet()
        data = data or []
        for obj in data:
            if obj:
                results.append(cls.parse(obj))
        return results

    def __repr__(self):
        items = filter(lambda x: x[0] in self._repr_values.keys(), vars(self).items())
        state = ['%s: %s' % (self._repr_values[k], repr(v)) for (k, v) in items]
        return '<%s: %s >' % (self.__class__.__name__, ', '.join(state))


class Article(Model):
    _not_found_error_class = errors.ArticleNotFound

    def __init__(self, **kwargs):
        super(Article, self).__init__(**kwargs)
        self._repr_values = {"id": "ID", "title": "Title"}


class Column(Model):
    _not_found_error_class = errors.ArticleNotFound

    def __init__(self, **kwargs):
        super(Column, self).__init__(**kwargs)
        self._repr_values = {"id": "ID", "title": "Title"}
