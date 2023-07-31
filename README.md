# Парсер новостных сайтов

![Логотип Парсера новостных сайтов](https://www.nur.kz/nur/img/logo.svg)
![Логотип Парсера новостных сайтов](https://scientificrussia.ru/assets/6bec6da9/logo.svg)

**Парсер новостных сайтов** - это инструмент для извлечения данных из различных новостных сайтов и сохранения их в базе данных SQLite. Этот проект позволяет получать информацию о новостях с выбранных веб-ресурсов.

## Установка и настройка

1. Клонируйте репозиторий на ваш компьютер:

    git clone https://github.com/Azamatsksstv/ParserProject


Создайте виртуальное окружение и активируйте его:
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate

Установите зависимости из файла requirements.txt:
    pip install -r requirements.txt

Создайте базу данных db.db и таблицы items и resource:

Использование
Отредактируйте файл queries.py, чтобы настроить таблицы items и resource в соответствии с вашими потребностями.

Запустите парсинг данных новостей:
python main.py
