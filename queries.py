import sqlite3


def drop_table_items():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''drop table items;''')
    except Exception as ex:
        print(ex)


def create_table_items():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''create table items
                            (id integer primary key autoincrement,
                            res_id int,
                            link text not null, 
                            title text not null, 
                            content text not null ,
                            nd_date int(11),
                            s_date int(11),
                            not_date date not null);''')
        connection.close()
    except Exception as ex:
        print(ex)


def insert_to_items(data):
    try:
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = '''INSERT INTO items (res_id, link, title, content, nd_date, s_date, not_date) VALUES (?, ?, ?, ?, ?, ?, ?)'''
        values = data
        cursor.executemany(query, values)
        connection.commit()
        connection.close()
        print("success")
    except Exception as ex:
        print(ex)


def drop_table_resource():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''drop table resource;''')
    except Exception as ex:
        print(ex)


def create_table_resource():
    try:
        connection = sqlite3.connect('db.db')
        connection.execute('''create table resource
                            (RESOURCE_ID  integer primary key autoincrement,
                            RESOURCE_NAME  varchar(255),
                            RESOURCE_URL  varchar(255), 
                            top_tag  varchar(255),
                            bottom_tag  varchar(255),
                            title_cut  varchar(255),
                            date_cut  varchar(255));''')
        connection.close()
        print("success")
    except Exception as ex:
        print(ex)


def insert_to_resource(datas):
    try:
        connection = sqlite3.connect('db.db')
        cursor = connection.cursor()
        query = '''INSERT INTO resource (RESOURCE_NAME, RESOURCE_URL, top_tag, bottom_tag, title_cut, date_cut) VALUES (?, ?, ?, ?, ?, ?)'''
        values = datas
        cursor.executemany(query, values)
        connection.commit()
        connection.close()
        print("inserted to resource")
    except Exception as ex:
        print(ex)


def get_resource_id(res_name):
    try:
        connection = sqlite3.connect('db.db')
        cursor = connection.execute('''select RESOURCE_ID from resource where RESOURCE_NAME = ?''', (res_name,))
        results = cursor.fetchall()
        if results:
            resource_id = results[0][0]
        else:
            resource_id = None
        connection.close()
        return resource_id
    except Exception as ex:
        print(ex)
