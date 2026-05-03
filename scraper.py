import requests
from bs4 import BeautifulSoup
import time

base_url = "http://quotes.toscrape.com"
url = base_url
all_quotes = []

while url:
    print(f"Scraping {url}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        all_quotes.append((text, author))

    next_button = soup.find("li", class_="next")
    if next_button:
        next_link = next_button.find("a")["href"]
        url = base_url + next_link
        time.sleep(1)
    else:
        url = None

print(f"\nDone! Total quotes scraped: {len(all_quotes)}")

with open("quotes.txt", "w") as f:
    for text, author in all_quotes:
        f.write(f"{text} — {author}\n\n")

print("Saved everything to quotes.txt!")