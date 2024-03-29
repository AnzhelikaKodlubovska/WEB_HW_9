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
            quotes.append({"quote": text, "author": author, "tags": tags})
        page += 1
    return quotes


def scrape_authors():
    authors_info = []
    page = 1
    while True:
        response = requests.get(f"{url}/page/{page}/")
        soup = BeautifulSoup(response.text, "html.parser")
        authors_list = soup.find_all("div", class_="quote")
        if not authors_list:
            break
        for author_item in authors_list:
            author_name = author_item.find("small", class_="author").text
            author_description = author_item.find("span", class_="text").text
            authors_info.append({"fullname": author_name, "description": author_description})
        page += 1
    return authors_info






def write_to_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    quotes_data = scrape_quotes()
    write_to_json(quotes_data, "quotes.json")
    
    authors_data = scrape_authors()
    write_to_json(authors_data, "authors.json")
