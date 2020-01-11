# Crawl/Index/Search IMDB Top 1000

A library for crawling, indexing and searching top-1000 imdb listing.

See individual files for module desciprtions.

## Installation

Install dependencies with [Python pip](https://pypi.org/project/pip/):

`pip install -r requirements.pip`

## Usage

First build the movies index. This only needs to be done once and the result is
cached on disk:

`python main.py --rebuild-index`

Query the index:

```
$ python main.py spielberg
['Bridge of Spies', 'Catch Me If You Can', 'Close Encounters of the Third Kind', 'E.T. the Extra-Terrestrial', 'Empire of the Sun', 'Indiana Jones and the Last Crusade', 'Indiana Jones and the Temple of Doom', 'Jaws', 'Jurassic Park', 'Minority Report', 'Munich', 'Raiders of the Lost Ark', 'Saving Private Ryan', "Schindler's List", 'The Color Purple', 'The Goonies']
$ python main.py spielberg hanks
['Bridge of Spies', 'Catch Me If You Can', 'Saving Private Ryan']`
```



