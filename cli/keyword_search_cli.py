#!/usr/bin/env python3
import argparse
from lib.keyword_search import search_command

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparser = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparser.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    subparser.add_parser("build", help="Build the inverted index")

    args = parser.parse_args()
    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            results = search_command(args.query)
            for num, res in enumerate(results, start=1):
                print(f"{num}. {res}")
        case "build":
            print("Build the inverted index")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()