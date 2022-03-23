from flask import Flask, render_template, redirect, request, session, g, Blueprint, jsonify
import json
import os
import urllib3
import sqlite3
import time
from db import init_db
import auth
import matchhistory
import wordle

app = Flask(__name__)

app.secret_key = os.urandom(32),
DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
db = sqlite3.connect(DATABASE, check_same_thread=False)
c = db.cursor()

init_db()

app.register_blueprint(auth.bp)

app.register_blueprint(matchhistory.bp)

@app.route("/", methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        redirect("/login")

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
