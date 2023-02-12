import sqlite3

import dateparser
import datetime
import queries
import requests
from bs4 import BeautifulSoup


def parse():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM resource')
    rows = cursor.fetchall()
    resource_id = 0

    response = requests.get(rows[resource_id][2])
    soup = BeautifulSoup(response.text, "lxml")
    news = soup.findAll('article', class_='block-infinite__item-content')

    data = []
    res_id = str(queries.get_resource_id(rows[resource_id][1]))
    for news_item in news:
        link = news_item.find(rows[resource_id][3]).get('href')                           # ссылку на новость
        title = news_item.find(rows[resource_id][5]).text.strip()                         # заголовок новости.

        response_news_item = requests.get(link)
        soup_news_item = BeautifulSoup(response_news_item.text, "lxml")
        content_items = soup_news_item.findAll('p', class_='align-left formatted-body__paragraph')
        content = ''.join(i.text for i in content_items)

        datetime_from_website = news_item.find(rows[resource_id][6]).text.strip()
        timestamp = dateparser.parse(datetime_from_website)
        nd_date = datetime.datetime.timestamp(timestamp) * 1000                 # дату и время новости в формате Unix time
        current_time = datetime.datetime.now()
        s_date = datetime.datetime.timestamp(current_time) * 1000               # дату и время попадания новости в саму таблицу items в формате Unix time
        not_date = timestamp.strftime("%Y-%m-%d")                               # дату новости в формате Год-Месяц-День
        data.append([res_id, link, title, content, nd_date, s_date, not_date])

    queries.insert_to_items(data)


def main():
    queries.drop_table_items()
    queries.create_table_items()
    parse()


if __name__ == '__main__':
    main()
