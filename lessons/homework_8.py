import sqlite3


connection = sqlite3.connect("../library.db")


def create_table():
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    connection.commit()


def insert_books():
    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 122, 5),
        ("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 3),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 4),
        ("Белый пароход", "Чингиз Айтматов", 1970, "Повесть", 160, 2)
    ]

    connection.executemany("""
        INSERT INTO books (
            name,
            author,
            publication_year,
            genre,
            number_of_pages,
            number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()


def get_books_by_author(author):
    cursor = connection.execute(
        "SELECT * FROM books WHERE author = ?",
        (author,)
    )

    books = cursor.fetchall()

    if books:
        for book in books:
            print(book)
    else:
        print("Книги этого автора не найдены")


def delete_book_by_id(id):
    cursor = connection.execute(
        "DELETE FROM books WHERE id = ?",
        (id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Книга удалена")
    else:
        print("Книга с таким ID не найдена")


create_table()
insert_books()

get_books_by_author("Лев Толстой")

delete_book_by_id(1)

connection.close()