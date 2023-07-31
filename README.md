# Парсер новостных сайтов

![Логотип Парсера новостных сайтов](https://www.nur.kz/nur/img/logo.svg)
![Логотип Парсера новостных сайтов](https://scientificrussia.ru/assets/6bec6da9/logo.svg)

**Парсер новостных сайтов** - это инструмент для извлечения данных из различных новостных сайтов и сохранения их в базе данных SQLite. Этот проект позволяет получать информацию о новостях с выбранных веб-ресурсов.

## Установка и настройка

1. Клонируйте репозиторий на ваш компьютер:
<pre>
    git clone https://github.com/Azamatsksstv/ParserProject
</pre>

Создайте виртуальное окружение и активируйте его:
<pre>
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
</pre>


Установите зависимости из файла requirements.txt:
<pre>
    pip install -r requirements.txt
</pre>

Создайте базу данных db.db и таблицы items и resource

Запустите парсинг данных новостей:
<pre>
    python main.py
</pre>

После выполнения, данные с веб-ресурсов будут сохранены в таблицу items.

*Пример использования*
В таблице resource добавили url новостных сайтов NUR.KZ и Научная Россия
![image](https://github.com/Azamatsksstv/ParserProject/assets/90980633/28ee395a-8170-4e17-b344-64b7d36d7de2)

Успешно заранили код main.py
![image_2023-07-31_07-51-38](https://github.com/Azamatsksstv/ParserProject/assets/90980633/0053b382-e27e-4bda-a184-f985d56b068e)

В таблице items получили результат парсинга
![image](https://github.com/Azamatsksstv/ParserProject/assets/90980633/3c466c06-3a3e-45f3-81c8-1d11997fecef)
