import records
from flask import Flask, jsonify
app = Flask(__name__)
db = records.Database("postgres://localhost/sports_db")

teams = db.query("SELECT * FROM sports_stats;")

#first part of homework
@app.route("/first")
def show_html():
    return "<div>Hello world!</div>"

#updated to output JSON instead of HTML
@app.route("/second")
def show_json():
    list = [1, 2, 3, "this is a string"]
    return jsonify(list)
