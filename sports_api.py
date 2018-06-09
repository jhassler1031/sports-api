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
#=========================================================================

@app.route("/")
def show_teams():
    return db.query("SELECT * FROM sports_stats;").export('json')

#==========================================================================
#long way below
"""
@app.route("/")
def show_teams():
    teams = db.query("SELECT * FROM sports_stats;")
    team_list = []
    for team in teams:
        team = team.as_dict()
        row_list = {}
        for key, value in team.items():
            if str(value).isdigit():
                value = int(value)
            row_list[key] = value
        team_list.append(row_list)
    return jsonify(team_list)



teams = db.query("SELECT * FROM sports_stats;")
team_list = []
for team in teams:
    team = team.as_dict()
    row_list = {}
    for key, value in team.items():
        if str(value).isdigit():
            value = int(value)
        row_list[key] = value
    team_list.append(row_list)
print(team_list)
"""
