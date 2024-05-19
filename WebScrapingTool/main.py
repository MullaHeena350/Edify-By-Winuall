import requests
from bs4 import BeautifulSoup
import csv

# URL of the website you want to scrape
URL = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
r = requests.get(URL)

# Parse the page content
soup = BeautifulSoup(r.content, 'html.parser')

# List to store book details
books = []

# Find all book items on the page
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    stock = book.find('p', class_='instock availability').text.strip()

    # Append book details to the list
    books.append({
        'title': title,
        'price': price,
        'stock': stock
    })

# Write the book details to a CSV file
filename = 'books.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['title', 'price', 'stock'])
    w.writeheader()
    for book in books:
        w.writerow(book)

print(f'Successfully scraped {len(books)} books.')
