from bs4 import BeautifulSoup as soup
import requests
import cloudscraper

url = 'https://www.buzzsneakers.bg/obuvki/?search=jordan'

scraper = cloudscraper.create_scraper(delay=10, browser='chrome')

result = scraper.get(url).text
magic = soup(result, 'html.parser')

something = magic.find_all('div', class_='title')

# list = []
#
# for item in something:
#     a_tags = item.find_all('a')
#     list.append(str(a_tags))
#
# for item in list:
#     if 'JORDAN' in item:
#         print(item)

dunno = magic.find_all('div', class_='current_price')
print(dunno)
