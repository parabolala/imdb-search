"""Contains FileBackedDict a dict that can be flushed to/loaded from disk."""
import os
import os.path
import pickle


class FileBackedDict(dict):
    """File-backed cache implementation.

    On init loads cache from file if available.
    On save() writes new cache state to disk.
    """
    def __init__(self, fname):
        super().__init__()
        self._fname = fname
        if os.path.exists(fname):
            self.update(pickle.load(open(fname, 'rb')))

    def save(self):
        tmp_file = self._fname + '.tmp'
        with open(tmp_file, 'wb') as f:
            pickle.dump(self, f)
        os.rename(tmp_file, self._fname)
