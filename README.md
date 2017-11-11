# python-hurriyet

A library that provides a Python interface to [Hurriyet API](https://developers.hurriyet.com.tr).

## Installation

The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install python-hurriyet

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/yakupadakli/python-hurriyet.git
    cd python-hurriyet
    python setup.py install

Python 2.7, 3.5 and 3.6, is supported for now.

## Usage

    from hurriyet.api import Api
    api_key = ""
    api = Api(api_key)

### Article

##### Article list

A list of all articles.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| article_id  | The article’s ID.  | optional |
| modified_date  | The article’s modified date.  | optional |
| path  | The article’s path.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.article.all()

##### Show get

Retrieve information for a given article.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| article_id  | The article’s ID.  | required |


    api.article.get("40199111")


### Column

##### Column list

A list of all columns.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| column_id  | The column’s ID.  | optional |
| writer_id  | The writer’s ID.  | optional |
| modified_date  | The column’s modified date.  | optional |
| path  | The column’s path.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.column.all()

##### Column get

Retrieve information for a given column.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| column_id  | The column’s ID.  | required |


    api.column.get("40190106")
