from flask import Flask, render_template, request, redirect
from database import create_database
import sqlite3
from datetime import datetime

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY id DESC")
    expenses = cursor.fetchall()

    connection.close()

    return render_template("index.html", expenses=expenses)


@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    description = request.form["description"]

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
        """,
        (amount, category, description, date)
    )

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)