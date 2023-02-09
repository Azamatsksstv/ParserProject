from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
try:
    os.remove("C:/Users/AZAMAT/Desktop/data.csv")
except Exception as ex:
    ...

url = 'https://www.nur.kz/society/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

news = soup.findAll('article', class_='block-infinite__item-content')
# print(news)

data = []
for news_item in news:
    link = news_item.find('a', class_='article-preview-mixed article-preview-mixed--secondary article-preview-mixed--with-absolute-secondary-item js-article-link').get('href')
    response_of_news = requests.get(link)
    soup_of_news = BeautifulSoup(response_of_news.text, "lxml")
    zagolovok = soup_of_news.find('h1', class_="main-headline js-main-headline").text
    content_of_news = soup_of_news.find('div', class_="page__reducer js-page-content")
    date_of_news = soup_of_news.find('time', class_="datetime datetime--publication").text
    data.append([link, zagolovok, content_of_news, date_of_news])

#
# # print(data)
header = ['link', 'zagolovok', 'content_of_news', 'date_of_news']
df = pd.DataFrame(data, columns=header)
df.to_csv('C:/Users/AZAMAT/Desktop/data.csv', sep=';', encoding='utf8')
