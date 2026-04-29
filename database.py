import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS mytable (
    id INTEGER PRIMARY KEY,
    name TEXT,
    value REAL
)
''')

cursor.execute("INSERT INTO mytable (name, value) VALUES (?, ?)", ('example', 123.45))

cursor.execute("SELECT * FROM mytable")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()