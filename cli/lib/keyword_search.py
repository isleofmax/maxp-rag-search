from .config import ITEM_LIMIT, MOVIE_FILE, STOP_WORDS_FILE
import json
import string
from nltk.stem import PorterStemmer

def search_command(query) -> list[str]:
    list_movie   = []
    query_tokens = []
    title_tokens = []
    n_movies = 1
    stemmer = PorterStemmer()
    preprocessed_words = preprocess_list_words(read_stop_words())
    preprocessed_query = preprocess_str(query)
    query_tokens = tokenize_str(preprocessed_query)
    query_tokens = filter_tokens(query_tokens, preprocessed_words)
    query_stemmed_tokens = stem_tokens(stemmer, query_tokens)

    with open(MOVIE_FILE,"r") as file:
        json_data = json.load(file)
        for movie in json_data.get("movies"):
            movie_title = movie.get("title")
            preprocessed_title = preprocess_str(movie_title)
            title_tokens = tokenize_str(preprocessed_title)
            title_tokens = filter_tokens(title_tokens, preprocessed_words)
            stemmed_tokens = stem_tokens(stemmer, title_tokens)
            if test_tokens(query_stemmed_tokens, stemmed_tokens):
                if n_movies > ITEM_LIMIT:
                    break
                list_movie.append(movie_title)
                n_movies += 1
                
    return list_movie


def read_stop_words() -> list[str]:
    words = []
    with open(STOP_WORDS_FILE, "r") as f:
        words = f.read().splitlines()
    return words


def preprocess_list_words(words: list[str]) -> list[str]:
    pword = []
    for word in words:
        pword.append(preprocess_str(word))
    return pword


def preprocess_str(s: str) -> str:
    return s.lower().translate(str.maketrans("", "", string.punctuation))


def tokenize_str(s: string) -> list[str]:
    return set(s.split())


def filter_tokens(input_tokens: list[str], stop_words: list[str]) -> list[str]:
    output_list = []
    for itoken in input_tokens:
        try:
            stop_words.index(itoken)
        except:
            output_list.append(itoken)

    return output_list


def stem_tokens(stemmer: PorterStemmer, tokens: list[str]) -> list[str]:
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    return stemmed_tokens


def test_tokens(query: list[str], title: list[str]) -> bool:
    for qword in query:
        for tword in title:
            if qword in tword:
                return True
    return False
