from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


try:
    os.remove("C:/Users/AZAMAT/Desktop/data.xlsx")
except Exception as ex:
    ...

url = 'https://www.nur.kz/society/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

films = soup.findAll('article', class_='block-infinite__item-content')

print(len(films))

data = []
for film in films:
    # print(film)
    link = film.find('a').get('href')
    # print(link)

    datetime_of_news = film.find('time').text.strip()
    # print(datetime_of_news)

    zagolovok_of_news = film.find('h3').text.strip()
    # print(zagolovok_of_news)

    data.append([link, zagolovok_of_news, datetime_of_news])

print(data)

header = ['link', 'datetime_of_news', 'zagolovok_of_news']
df = pd.DataFrame(data, columns=header)
df.to_excel('C:/Users/AZAMAT/Desktop/data.xlsx', sheet_name='Your sheet name', index=False)

