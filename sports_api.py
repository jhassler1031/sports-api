import records
from flask import Flask, jsonify
app = Flask(__name__)
db = records.Database("postgres://localhost/sports_db")

teams = db.query("SELECT * FROM sports_stats;")

@app.route("/")
def show_teams():
    return "<div>Hello world!</div>"
