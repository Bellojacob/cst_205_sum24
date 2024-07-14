from bs4 import BeautifulSoup
from urllib.request import urlopen

site = "https://www.amazon.com/gp/product/B0BRM67RN9/ref=ox_sc_act_title_1?smid=ATVPDKIKX0DER&psc=1"

site_html = urlopen(site)
soup = BeautifulSoup(site_html.read(), 'lxml')

print(soup.title.text)

price =soup.find_all('a-price-whole')
print(price)