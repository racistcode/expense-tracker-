from database import connect_db


def add_expense(amount, category, description):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (amount, category, description)
        VALUES (?, ?, ?)
        """,
        (amount, category, description)
    )

    connection.commit()
    connection.close()