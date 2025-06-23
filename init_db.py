import sqlite3

conn = sqlite3.connect('attendance_system.db')
cursor = conn.cursor()

cursor.execute('''
    DELETE FROM users WHERE name = ?;
''', ('Kujan',))

conn.commit()
conn.close()