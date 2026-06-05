from .config import MOVIE_FILE, INDEX_FILE, DOCMAP_FILE
from .keyword_search import filter_tokens, preprocess_str, preprocess_list_words, read_stop_words, tokenize_str 
import json

class InvertedIndex():
    def __init__(self):
        self.index: dict[str, set[int]] = {}
        self.docmap: dict[int, object] = {}

    def __add_document(self, doc_id, text) -> None:
        for token in filter_tokens(tokenize_str(preprocess_str(text)), preprocess_list_words(read_stop_words())):
            if token in self.index.keys():
                if doc_id not in self.index[token]:
                    self.index[token].append(doc_id)
            else:
                self.index[token] = [doc_id]

    def get_documents(self, term) -> list[int]:
        return list(sorted(self.index[term.lower()]))

    def build(self) -> None:
        with open(MOVIE_FILE, "r") as file:
            json_data = json.load(file)
            for movie in json_data["movies"]:
                doc_id = movie["id"]
                self.__add_document(doc_id, f"{movie['title']} {movie['description']}")
                self.docmap[doc_id] = movie
    
    def save(self) -> None:
        with open(INDEX_FILE, "w") as file:
            json.dump(self.index, file)

        with open(DOCMAP_FILE, "w") as file:
            json.dump(self.docmap, file)

        