import requests
from bs4 import BeautifulSoup


Base_url = "https://in.tradingview.com/symbols/XETR-DAX/"

# Load the page and sent to HTML parse
page = requests.get(Base_url)
#print(page)
soup = BeautifulSoup(page.content, 'html.parser')
all_div = soup.find_all('header', class_="tv-category-header")

#print(all_div)
for div in all_div:
    all_items = div.find_all('div', class_ = "tv-symbol-price-quote")
    #print(all_items)
    for item in all_items:
        price = item.find('div', {"class": "tv-symbol-price-quote__value"})
        print(price)
      