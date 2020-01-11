"""Term indexing mechanism."""
import re
from typing import List

from common import FileBackedDict

WORD_STEM_RE = re.compile('[^a-zA-Z0-9]+')


def word_terms(word: str) -> List[str]:
    """Extracts list of index terms from a string."""
    return WORD_STEM_RE.sub(' ', word).lower().split()


class Index:
    def __init__(self, cache_fname):
        self._index = FileBackedDict(cache_fname)

    def add(self, doc_id, terms):
        for term in terms:
            if term not in self._index:
                self._index[term] = []
            if doc_id not in self._index[term]:
                self._index[term] = self._index[term] + [doc_id]

    def lookup(self, query):
        return self._lookup_terms(word_terms(query))

    def _lookup_terms(self, terms):
        if not terms:
            return []
        candidates = None
        for term in terms:
            if term not in self._index:
                return []
            if candidates is None:
                candidates = set(self._index[term])
            candidates &= set(self._index[term])
        return candidates
