import sqlite3


def connect_db():
    connection = sqlite3.connect("expenses.db")
    return connection


def create_table():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()