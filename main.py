from bs4 import BeautifulSoup
import requests
import queries

url = 'https://www.nur.kz/society/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
films = soup.findAll('article', class_='block-infinite__item-content')
data = []

for film in films:
    link = film.find('a').get('href')
    title = film.find('h3').text.strip()
    datetime = film.find('time').text.strip()
    data.append([link, title, datetime])


queries.drop_table_resource()
queries.create_table_resource()
queries.insert_to_resource(data)
