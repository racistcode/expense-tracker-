from flask import Flask, render_template
from database import create_database

app = Flask(__name__)

# Create the database and expenses table
create_database()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)