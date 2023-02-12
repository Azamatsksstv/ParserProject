import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM resource')
rows = cursor.fetchall()

for row in rows:
    print(row)

# close the cursor and connection
cursor.close()
conn.close()
