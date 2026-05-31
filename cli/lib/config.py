import os

ITEM_LIMIT = 5
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MOVIE_FILE = os.path.join(PROJECT_ROOT, "data", "movies.json")
STOP_WORDS_FILE = os.path.join(PROJECT_ROOT, "data", "stopwords.txt")
INDEX_FILE = os.path.join(PROJECT_ROOT, "cache", "index.pkl")
DOCMAP_FILE = os.path.join(PROJECT_ROOT, "cache", "docmap.pkl")