import requests
from bs4 import BeautifulSoup

url = 'https://www.nur.kz/society/'
page = requests.get(url)

bs = BeautifulSoup(page.content, 'html.parser')

news_articles = bs.find_all('div', class_='page__reducer js-page-content')

print(news_articles)
# Extract the title and summary of each article
# for article in news_articles:
#     title = article.find('h3', class_='news-item__title').text
#     summary = article.find('div', class_='news-item__desc').text
#
#     print(title)
#     print(summary)
#     print('---')
