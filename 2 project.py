import sqlite3

connection = sqlite3.connect('school_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        class TEXT NOT NULL,
        mark INTEGER,
        attendance TEXT
    )
''')
connection.commit()

def ask_action():
    return input(
        'Это журнал. Выберите действие:\n'
        '1 — добавить ученика\n'
        '2 — посмотреть список\n'
        '0 — закончить\n'
        'Ваш выбор: '
    )

start = ask_action()

while True:
    if start == "1":
        surname = input('Введите фамилию ученика: ')
        class_name = input('Введите класс ученика: ')

        try:
            mark = int(input('Введите оценку ученика: '))
        except ValueError:
            print('Оценка должна быть числом.')
            start = ask_action()
            continue

        attendance = input('Введите был ли ученик на уроке: ')

        cursor.execute(
            'INSERT INTO users (name, class, mark, attendance) VALUES (?, ?, ?, ?)',
            (surname, class_name, mark, attendance)
        )
        connection.commit()
        print(f'Ученик {surname} добавлен')
        start = ask_action()

    elif start == "2":
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print('Список пуст.')

        start = ask_action()

    elif start == "0":
        connection.close()
        break

    else:
        print('Неверный ввод.')
        start = ask_action()