import records
from flask import Flask, jsonify
app = Flask(__name__)
db = records.Database("postgres://localhost/sports_db")

#first part of homework
@app.route("/first")
def show_html():
    return "<div>Hello world!</div>"

#updated to output JSON instead of HTML
@app.route("/second")
def show_json():
    list = [1, 2, 3, "this is a string"]
    return jsonify(list)

#Display data from sports_stats table in sports_db
@app.route("/")
def show_teams():
    teams = db.query("SELECT * FROM sports_stats;")
    team_list = []
    for team in teams:
        row_list = []
        for item in team:
            row_list.append(str(item))
        team_list.append(row_list)
    return jsonify(team_list)

"""
teams = db.query("SELECT * FROM sports_stats;")
team_list = teams.as_dict()
print*(team_list)
"""
