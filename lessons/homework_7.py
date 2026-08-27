import sqlite3


connection = sqlite3.connect("../library.db")


def create_table():
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
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
        ("Война и мир", "Лев Толстой", 1869, "Роман", 122)
        ]