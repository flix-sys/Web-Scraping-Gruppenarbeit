# Importiere die benötigten Bibliotheken
import pandas as pd  # Für die Arbeit mit Tabellen
import requests  # Um HTTP-Anfragen zu senden
from pyquery import PyQuery as pq

# URL der Webseite, die wir scrapen wollen
url = "https://books.toscrape.com/catalogue/category/books_1/page-1.html"

# Sende eine HTTP GET-Anfrage an die Webseite
response = requests.get(url)

# Hole den HTML-Inhalt der Seite als Text
html = response.text

# Erstelle ein PyQuery-Objekt, um das HTML zu durchsuchen
doc = pq(html)

# Leere Liste, zum speichern
books = []

# Durchsuche alle <a>-Tags innerhalb von <h3>-Tags
# Auf dieser Seite enthält jedes <h3> den Buchtitel als Link
for link in doc("h3>a").items():
    # Extrahiere den Titel aus dem "title"-Attribut
    title = link.attr("title")

    # Extrahiere den Link aus dem "href"-Attribut
    href = link.attr("href")

    # Füge die Daten als Dictionary zur Liste hinzu
    books.append({"Title": title, "Links": href})

# Erstelle ein Pandas DataFrame aus der Liste der Bücher
df = pd.DataFrame(books)

# Zeige das DataFrame an
print(df)