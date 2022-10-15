from bs4 import BeautifulSoup
import requests
import csv


URL = "https://www.audible.com/search?keywords=book&node=18573211011"
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_book = soup.select(selector="h3 .bc-link")

for book in all_book:
    print(book.getText())

# print(len(all_book))
