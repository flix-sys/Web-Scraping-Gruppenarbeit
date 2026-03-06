import pandas as pd
import requests
from pyquery import PyQuery as pq

doc = pq(url="https://books.toscrape.com/catalogue/category/books_1/page-1.html")


for link in doc("h3>a"):
    print(link.text, link.attrib["href"])

