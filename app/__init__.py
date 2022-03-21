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

def create_app():
    app = Flask(__name__)
    # Configure app key & DB location
    app.config.from_mapping(
        SECRET_KEY = os.urandom(32),
        DATABASE = os.path.join(app.instance_path, db.DB_FILE)
    )
    # Ensure the DB location exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

app.register_blueprint(auth.bp)

app.register_blueprint(matchhistory.bp)


with app.app_context():
    db.init_db()
    d = db.get_db()
    c = d.cursor()

@app.route("/")
def home():
    if request.method == 'POST':
        input = request.get_json().get('input')
        input = json.loads(input)
        input = json.dumps(input)
        wordle.guess(input)
    else:
        return render_template("home.html")

@app.route("/leaderboard")
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

if __name__ == "__main__":
    app.debug = True
    app.run()
