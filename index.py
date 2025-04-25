import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
books = soup.select(".product_pod")

with open("books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Tên", "Giá", "Đánh giá"])

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        rating = book.p["class"][1]
        writer.writerow([title, price, rating])
