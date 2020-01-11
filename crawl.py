"""Crawler classes for fetching and parsing IMDB pages."""
from typing import List, Optional
from urllib.request import urlopen
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class Page:
    """Helper class for fetching and parsing HTML pages."""

    def __init__(self, url: str):
        self.url = url
        self._bs = None

    def _fetch(self):
        print("Fetching %s" % self.url)
        html = urlopen(self.url).read()
        return BeautifulSoup(html, 'html.parser')

    @property
    def bs(self) -> BeautifulSoup:
        """Parses and return a BeautifulSoup object."""
        if self._bs is None:
            self._bs = self._fetch()
        return self._bs

    def __repr__(self):
        return '<%s: %s >' % (self.__class__.__name__, self.url)


class ListingPage(Page):
    def get_next_page(self) -> Optional['ListingPage']:
        next_as = self.bs.find_all('a', class_='next-page')
        if not next_as:
            return None
        return ListingPage(urljoin(self.url, next_as[0].attrs['href']))

    def get_movie_pages(self) -> List['MoviePage']:
        res = []
        for a in self.bs.select('.lister-item-content h3 a'):
            res.append(MoviePage(urljoin(self.url, a.attrs['href'])))
        return res


class MoviePage(Page):
    @property
    def title(self):
        return self.bs.find('h1').find(text=True).strip()

    def get_basic_credits(self) -> List[str]:
        return sorted({
            a.text for a in self.bs.select('div.credit_summary_item a')
            if '/name/' in a.attrs['href']
        })

    def get_full_credits(self):
        # TODO: parse https://www.imdb.com/title/%d/fullcredits
        return []
