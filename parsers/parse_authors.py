
import json

def parse_authors(quotes_json):
    quotes = json.load(open(quotes_json))

    authors = set()
    for quote in quotes:
        authors.add(quote["author"])

    return list(authors)
