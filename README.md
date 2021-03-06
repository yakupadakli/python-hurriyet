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
| page_id  | The page’s ID.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.page.all()

##### Page get

Retrieve information for a given page.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| page_id  | The page’s ID.  | required |


    api.page.get("5581488665345c152c269bc0")


### Path

##### Path list

A list of all paths.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| path_id  | The path’s ID.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.path.all()

##### Path get

Retrieve information for a given path.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| path_id  | The path’s ID.  | required |


    api.path.get("563cddcc67b0a934e44ee2d7")


### Writer

##### Writer list

A list of all writers.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| writer_id  | The writer’s ID.  | optional |
| top  | Filters the number of records in the returned result set.  | optional |
| skip  | Skip the desired record from the result set.  | optional |


    api.writer.all()

##### Writer get

Retrieve information for a given writer.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| writer_id  | The writer’s ID.  | required |


    api.writer.get("57a8a3430f25441fb419c54a")


### Search

##### Search article

Retrieve articles for a given keyword.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| keyword  | Keyword.  | required |


    api.search.article("hurriyet")

##### Search column

Retrieve columns for a given keyword.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| keyword  | Keyword.  | required |


    api.search.column("hurriyet")

##### Search folder

Retrieve folders for a given keyword.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| keyword  | Keyword.  | required |


    api.search.folder("hurriyet")

##### Search news photo gallery

Retrieve news photo galleries for a given keyword.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| keyword  | Keyword.  | required |


    api.search.news_photo_gallery("hurriyet")

##### Search page

Retrieve pages for a given keyword.

| param  | Description |  |
| ------------- | ------------- | ------------- |
| keyword  | Keyword.  | required |


    api.search.page("hurriyet")
