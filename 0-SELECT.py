import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

queries = [
    'SELECT * FROM longlist;',
    'SELECT title FROM longlist;',
    'SELECT title, author FROM longlist;',
    'SELECT title, author, translator FROM longlist;'
]

for q in queries:
    print(f"\n🔹 Query: {q}")
    cursor.execute(q)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()