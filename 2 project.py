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
        while next != "0":
            surname = input('Введите фамилию ученика: ')
            cursor.execute('SELECT * FROM users WHERE name = ?', (surname,))
            class_name = input('Введите класс ученика: ')
            cursor.execute('SELECT * FROM users WHERE class = ?', (class_name,))
            mark = input('Введите оценку ученика: ')
            cursor.execute('SELECT * FROM users WHERE mark = ?', (mark,))
            attendance = input('Введите был ли ученик на уроке: ')
            cursor.execute('SELECT * FROM users WHERE attendance = ?', (attendance,))
            connection.commit()
            connection.close()
            print(f'Ученик {surname} добавлен')
            next = input("Хотите продолжить? \n"
                  "Введите 1 чтобы добавить ученика \n"
                  "Введите 2 чтобы посмотреть список \n"
                  "Введите 0 чтобы закончить список \n")
    elif start == "2":
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)



        

