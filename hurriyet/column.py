from datetime import datetime

from hurriyet.client import Client
from hurriyet.models import Column as ColumnModel


class Column(Client):
    """Hurriyet column operations."""

    def __init__(self, **kwargs):
        super(Column, self).__init__(**kwargs)
        self.base_url = "/columns"

    def all(self, column_id=None, writer_id=None, modified_date=None, path=None, top=None, skip=None):
        """
        Get list of columns.

        :return [Columns]: The Hurriyet Columns.
        """
        filter_data = None
        if column_id:
            filter_data = "Id eq '%s'" % column_id

        if writer_id:
            data = "WriterId eq '%s'" % writer_id
            if filter_data:
                filter_data += ' and %s' % data
            else:
                filter_data = data

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
        return ColumnModel.parse_list(result)

    def get(self, column_id):
        """
        Get a single column.

        :return [Column]: The Hurriyet Column.
        """
        url = "%s/%s" % (self.base_url, column_id)
        result = self._get(url)
        return ColumnModel.parse(result)
