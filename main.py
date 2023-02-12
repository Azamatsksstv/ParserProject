from bs4 import BeautifulSoup
import requests
import queries
import datetime
import dateparser


def parse():
    RESOURCE_NAME = 'NUR.KZ'
    RESOURCE_URL  = 'https://www.nur.kz/society/'
    top_tag = 'a'
    bottom_tag = 'div' #otirik
    title_cut = 'h3'
    date_cut = 'time'

    response = requests.get(RESOURCE_URL)
    soup = BeautifulSoup(response.text, "lxml")
    news = soup.findAll('article', class_='block-infinite__item-content')

    resource_data = [[RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut]]
    queries.insert_to_resource(resource_data)

    data = []
    res_id = str(queries.get_resource_id(RESOURCE_NAME))
    for news_item in news:
        link = news_item.find(top_tag).get('href')                           # ссылку на новость
        title = news_item.find(title_cut).text.strip()                        # заголовок новости.
        datetime_from_website = news_item.find(date_cut).text.strip()
        timestamp = dateparser.parse(datetime_from_website)
        nd_date = datetime.datetime.timestamp(timestamp) * 1000     # дату и время новости в формате Unix time
        current_time = datetime.datetime.now()
        s_date = datetime.datetime.timestamp(current_time) * 1000   # дату и время попадания новости в саму таблицу items в формате Unix time
        not_date = timestamp.strftime("%Y-%m-%d")                   # дату новости в формате Год-Месяц-День
        data.append([res_id, link, title, nd_date, s_date, not_date])

    queries.insert_to_items(data)


def main():
    queries.drop_table_items()
    queries.create_table_items()
    queries.drop_table_resource()
    queries.create_table_resource()

    parse()


if __name__ == '__main__':
    main()
