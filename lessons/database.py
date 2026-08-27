import sqlite3


def create_tables(connection):
    connection.execute("DROP TABLE IF EXISTS students")
    # делаем SQL запрос для создания таблицы students
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    ''')


def add_student(connection, name, age, city):
    # запрос чтобы добавить данные студента в таблицу students
    connection.execute(
        '''
            INSERT INTO students (name, age, city)
            VALUES (?, ?, ?)
        ''',
        (name, age, city)
    )
    connection.commit()


def get_all_students(connection):
    # запрос чтобы получать список студентов
    result = connection.execute("SELECT * FROM students")
    return result.fetchall()


def get_student_by_name(connection, name):
    result = connection.execute(
        "SELECT * FROM students WHERE name = ? AND age = 18",
        (name,)
    )
    return result.fetchall()


def get_student_by_id(connection, student_id):
    result = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    return result.fetchall()


def delete_student_by_name(connection, name):
    connection.execute(
        '''DELETE FROM students WHERE name = ?''',
        (name,)
    )
    connection.commit()


def delete_student_by_id(connection, student_id):
    connection.execute(
        '''DELETE FROM students WHERE id = ?''',
        (student_id,)
    )
    connection.commit()


def change_age(connection, student_id, new_age):
    connection.execute(
        '''UPDATE students SET age = ? WHERE id = ?''',
        (new_age, student_id)
    )
    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect("database.db")  # .sqlite, .sqlite3
    create_tables(conn)
    add_student(conn, "Igor", 30, "Bishkek")
    add_student(conn, "Эмир", 16, "Баткен")
    add_student(conn, "Байэл", 18, "Каракол")
    add_student(conn, "Байэл", 20, "Бишкек")
    print(get_all_students(conn))
    print(get_student_by_name(conn, "Байэл"))
    delete_student_by_name(conn, "Байэл")
    print("--- после удаления ---")
    for st in get_all_students(conn):
        print(st)

    delete_student_by_id(conn, 1)
    print("---После удаление по id---")
    print(get_all_students(conn))
    change_age(conn, 2, 17)
    print("---После обновления---")
    print(get_all_students(conn))