from bs4 import BeautifulSoup
import requests
import csv


URL = "https://www.audible.com/search?keywords=book&node=18573211011"
response = requests.get(url=URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")

all_book = soup.select(selector="h3 .bc-link")

with open("computer_and_tech_book.csv", mode="a", newline="\n") as data:
    writer = csv.writer(data)
    for book in all_book:
        writer.writerow(book)
