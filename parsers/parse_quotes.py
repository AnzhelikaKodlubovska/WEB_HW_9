
import json

def parse_quotes(quotes_json):
 
    quotes = json.load(open(quotes_json))

   
    processed_quotes_data = []
    for quote in quotes:
        processed_quote = {
            "text": quote["text"],
            "author": quote["author"],
            "tags": quote["tags"]
        }
        processed_quotes_data.append(processed_quote)
        
    return processed_quotes_data
