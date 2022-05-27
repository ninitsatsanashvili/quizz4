import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('Sci-fi.csv', "w", newline='\n')
f.write('Title, Year\n')
filee = csv.writer(f)
h = {'Accept-Language': 'en-US'}
page = 1
while page < 200:
    url = 'https://www.imdb.com/search/title/?title_type=tv_movie&genres=sci-fi&start=' + str(page)
    r = requests.get(url)

    soupy = BeautifulSoup(r.text, 'html.parser')
    soup = soupy.find('div', class_='lister-list')
    scifi_movies = soup.find_all('div', class_='lister-item')
    for each in scifi_movies:
        url = each.img.attrs.get('loadlate')
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        info = each.p.text
        print(info)

    filee.writerow([title, year])
    page += 50
    sleep(randint(15, 20))
