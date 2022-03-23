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

app = Flask(__name__)

app.secret_key = os.urandom(32),
DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
db = sqlite3.connect(DATABASE, check_same_thread=False)
c = db.cursor()

app.register_blueprint(auth.bp)

app.register_blueprint(matchhistory.bp)

with app.app_context():
    db.init_db()
    d = db.get_db()
    c = d.cursor()

@app.route("/", methods=['GET', 'POST'])
def home():
    # if 'request.method == 'POST':
    #     input = request.get_json()
    #     input = jsonify(input)
    #     print(input)
    #     wordle.guess(input)

    # else:
    #     return render_template("home.html")'

    if 'username' in session:
        return render_template("home.html")
    else:
        redirect("/login")

@app.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    return render_template("leaderboard.html")

@app.route("/play")
def play():
    if 'username' in session:
        if 'game' not in session:
            wordle.new_game(session)
        if request.method == 'POST':
            input = json.loads(input)
            input = json.dumps(input)
            wordle.guess(input)
            print(input)
            return jsonify(session['game'])

@app.route('/getdata', methods=['GET', 'POST'])
def getdata():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        a = request.get_json()
        print(a.get('data'))
        wordle.new_game(session)
        wordle.check(a.get('data'))

        s = ''
        for i in session['game']['colors']:
            if i == 0: #green
                s.append('g')
            elif i == 1: #yellow
                s.append('y')
            else: #gray
                s.append('b')
        
        return s

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

if __name__ == "__main__":
    app.debug = True
    app.run()
