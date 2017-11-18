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


### NewsPhotoGallery

##### NewsPhotoGallery list

A list of all news photo galleries.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| news_photo_gallery_id  | The news photo gallery’s ID.  | optional |
| modified_date  | The news photo gallery’s modified date.  | optional |
| path  | The news photo gallery’s path.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.news_photo_gallery.all()

##### NewsPhotoGallery get

Retrieve information for a given news photo gallery.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| news_photo_gallery_id  | The news photo gallery’s ID.  | required |


    api.news_photo_gallery.get("40190642")


### NewsVideo

##### NewsVideo list

A list of all news videos.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| news_video_id  | The news video’s ID.  | optional |
| modified_date  | The news video’s modified date.  | optional |
| path  | The news video’s path.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.news_video.all()

##### NewsPhotoGallery get

Retrieve information for a given news video.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| news_video_id  | The news video’s ID.  | required |


    api.news_video.get("40393187")


### Page

##### Page list

A list of all pages.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page_id  | The news page’s ID.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.page.all()

##### Page get

Retrieve information for a given news video.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| news_video_id  | The news video’s ID.  | required |


    api.page.get("5581488665345c152c269bc0")
