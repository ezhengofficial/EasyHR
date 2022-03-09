from flask import Flask, render_template, redirect, request, session, g
import json
import os
import urllib3
import sqlite3
import time

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
