from .config import MOVIE_FILE, INDEX_FILE, DOCMAP_FILE
from .keyword_search import filter_tokens
import json

class InvertedIndex():
    def __init__(self):
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id, text):
        for token in filter_tokens(text):
            if self.index[token]:
                self.index[token].append(doc_id)
            else:
                self.index[token] = doc_id

    def get_documents(self, term):
        return sorted(self.index[term.lower()])

    def build(self):
        with open(MOVIE_FILE, "r") as file:
            json_data = json.load(file)
            doc_id = 1
            for movie in json_data:
                self.__add_document(doc_id, f"{movie['title']} {movie['description']}")
                doc_id += 1
    
    def save(self):
        pass