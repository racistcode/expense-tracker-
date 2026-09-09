from database import connect_db


def get_expenses():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, amount, category, description
        FROM expenses
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses