from flask import Flask, render_template, redirect, request, session, g, Blueprint, jsonify
import json
import os
import urllib3
import sqlite3
import time
import db
import auth
import matchhistory
import wordle
from datetime import date

app = Flask(__name__)

app.secret_key = os.urandom(32),
DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
db = sqlite3.connect(DATABASE, check_same_thread=False)
c = db.cursor()

app.register_blueprint(auth.bp)

app.register_blueprint(matchhistory.bp)

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'username' in session:
        c.execute("""SELECT lastplayed FROM users WHERE username = ?;""",
                      (session.get('username')))
        if c.fetchone() != date.today():
            c.execute("""UPDATE users SET lastplayed = ? WHERE username = ?;""",
                  (date.today(), session.get('username')))
            

        return render_template("home.html")
    else:
        return redirect("/login")

@app.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    return render_template("leaderboard.html")

@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        a = request.get_json()
        print(a.get('data'))

        return "OK", 200
    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

if __name__ == "__main__":
    app.debug = True
    app.run()
