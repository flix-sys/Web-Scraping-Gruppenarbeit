import pandas as pd
import requests
from pyquery import PyQuery as pq

url = "https://books.toscrape.com/catalogue/category/books_1/page-1.html"
response = requests.get(url)
html = response.text

doc = pq(html)

books = []

for link in doc("h3>a").items():
   title = link.attr("title")
   href = link.attr("href")
   books.append({"Title": title, "Links": href})

df = pd.DataFrame(books)
print(df)

