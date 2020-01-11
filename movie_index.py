"""Contains an Index subclass specializing in movies data."""
import concurrent.futures
from typing import Set, Generator

from crawl import ListingPage, MoviePage
from index import Index, word_terms


START_URL = 'https://www.imdb.com/search/title/?groups=top_1000'

def every_movie_page() -> Generator[MoviePage, None, None]:
    listing_page = ListingPage(START_URL)
    while listing_page is not None:
        for p in listing_page.get_movie_pages():
            yield p
        listing_page = listing_page.get_next_page()

def extract_movie_terms(movie_page: MoviePage) -> Set[str]:
    terms = []
    terms.extend(word_terms(movie_page.title))
    for credit in movie_page.get_basic_credits():
        terms.extend(word_terms(credit))
    return movie_page.title, set(terms)


class MovieIndex(Index):
    def rebuild_index(self):
        movie_pages = every_movie_page()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(extract_movie_terms, movie)
                for movie in movie_pages]
            for i, f in enumerate(concurrent.futures.as_completed(futures)):
                if i > 0 and i % 10 == 0:
                    print("Indexed %d of %d movies" % (i, len(futures)))
                doc_id, terms = f.result()
                self.add(doc_id, terms)
        self._index.save()
