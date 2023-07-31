# Парсер новостных сайтов

![Логотип Парсера новостных сайтов](https://www.nur.kz/nur/img/logo.svg)
![Логотип Парсера новостных сайтов](https://scientificrussia.ru/assets/6bec6da9/logo.svg)

**Парсер новостных сайтов** - это инструмент для извлечения данных из различных новостных сайтов и сохранения их в базе данных SQLite. Этот проект позволяет получать информацию о новостях с выбранных веб-ресурсов.

## Установка и настройка

1. Клонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/Azamatsksstv/ParserProject
'''bash


Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
```bash

Установите зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```bash

Создайте базу данных db.db и таблицы items и resource:

Использование
Отредактируйте файл queries.py, чтобы настроить таблицы items и resource в соответствии с вашими потребностями.

Запустите парсинг данных новостей:
python main.py
