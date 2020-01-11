import os.path
import sys

from movie_index import MovieIndex


IDX_CACHE_FILE_PATH = os.path.join(os.path.dirname(__file__),
                                   'index_cache.dat')

def main(argv):
    idx = MovieIndex(IDX_CACHE_FILE_PATH)
    if '--rebuild-index' in argv:
        print("Rebuilding index..")
        idx.rebuild_index()
        argv.remove('--rebuild-index')
    print(sorted(idx.lookup(' '.join(argv))))

if __name__ == '__main__':
    main(sys.argv[1:])
