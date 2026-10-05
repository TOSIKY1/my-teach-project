import sqlite3

connection = sqlite3.connect('school_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class TEXT NOT NULL,
        mark INTEGER,
        attendance TEXT )
''')
start = input('Это журнал, здесь нужно заполнять информацию о учениках. \n'
              'Введите 1 чтбы добавить ученика \n'
              'Введите 2 чтобы посмотреть список \n'
              'Введите 0 чтобы закончить список \n')
while True:
    if start == "1":
        while start != "0":
            start = input('Введите фамилию ученика: ')
            cursor.execute('SELECT * FROM users WHERE name = ?', (start,))
            start = input('Введите класс ученика: ')
            cursor.execute('SELECT * FROM users WHERE class = ?', (start,))
            start = input('Введите оценку ученика: ')
            cursor.execute('SELECT * FROM users WHERE mark = ?', (start,))
            start = input('Введите был ли ученик на уроке: ')
            cursor.execute('SELECT * FROM users WHERE attendance = ?', (start,))
            connection.commit()
            connection.close()
            print(f'Ученик {start} добавлен')
    elif start == "2":
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)



        

