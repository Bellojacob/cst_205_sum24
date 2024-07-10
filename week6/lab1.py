# https://www.espn.com/

from bs4 import BeautifulSoup
from urllib.request import urlopen
from wordcloud import WordCloud


my_site = "https://racingnews365.com/perez-no-longer-sure-of-red-bull-seat-despite-contract-extension"

site_html = urlopen(my_site)
soup = BeautifulSoup(site_html.read(), 'lxml')

print(soup.title.text)

images = soup.find_all('img')

for image in images:
    # print(image['src'])
    pass

# image found for task 2:
# https://cdn.racingnews365.com/2024/Perez/_1092x683_crop_center-center_85_none/SI202407050261_hires_jpeg_24bit_rgb.jpg?v=1720286067

# task 3
# text = soup.find('div', {'class': 'content-field__redactor'})
# print(text)

text = soup.get_text()
wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.show()