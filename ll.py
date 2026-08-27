import sqlite3


def create_tables(connection):
    connection.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT
        )
    ''')


def add_student(connection, name, age, city):
    connection.execute('''
        INSERT INTO students (name, age, city)
        VALUES (?, ?, ?)
    ''', (name, age, city))

    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect("lessons/database.db")

    create_tables(conn)
    add_student(conn, "Igor", 30, "Bishkek")

    conn.close()
