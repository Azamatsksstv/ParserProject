import sqlite3


def drop_table_resource():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''drop table items;''')
    except Exception as ex:
        print(ex)


def create_table_resource():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''create table items
                            (id integer primary key autoincrement,
                             link text not null, 
                             title text not null, 
                             datetime date not null);''')
        connection.close()
    except Exception as ex:
        print(ex)


def insert_to_resource(data):
    try:
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = '''INSERT INTO items (link, title, datetime) VALUES (?, ?, ?)'''
        values = data
        cursor.executemany(query, values)
        connection.commit()
        connection.close()
        print("success")
    except Exception as ex:
        print(ex)

