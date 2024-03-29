import requests
from bs4 import BeautifulSoup
import json

url = "http://quotes.toscrape.com"


def scrape_quotes():
    quotes = []
    page = 1
    while True:
        response = requests.get(f"{url}/page/{page}/")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes_list = soup.find_all("div", class_="quote")
        if not quotes_list:
            break
        for quote_item in quotes_list:
            text = quote_item.find("span", class_="text").text
            author = quote_item.find("small", class_="author").text
            tags = [tag.text for tag in quote_item.find_all("a", class_="tag")]
            quotes.append({"text": text, "author": author, "tags": tags})
        page += 1
    return quotes


def scrape_authors():
    authors = set()
    page = 1
    while True:
        response = requests.get(f"{url}/page/{page}/")
        soup = BeautifulSoup(response.text, "html.parser")
        authors_list = soup.find_all("div", class_="quote")
        if not authors_list:
            break
        for author_item in authors_list:
            author = author_item.find("small", class_="author").text
            authors.add(author)
        page += 1
    return list(authors)


def write_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    quotes_data = scrape_quotes()
    write_to_json(quotes_data, "quotes.json")
    
    authors_data = scrape_authors()
    write_to_json(authors_data, "authors.json")
