import re
import requests
from bs4 import BeautifulSoup

def get_images(site):

    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    images = []
    for img in img_tags:
        images.append(img.get('src'))

    return images

images = get_images("https://www.washingtonpost.com/news/fact-checker/wp/2018/02/07/president-trumps-claim-that-wages-are-now-for-the-first-time-in-many-years-rising/?noredirect=on&utm_term=.471bc6de0d69")

print(images)
