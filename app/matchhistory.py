from flask import Flask, render_template, redirect, request, session, g, Blueprint
import json
import os
import urllib3
import sqlite3
from datetime import date
from db import get_db

bp = Blueprint('matchhistory', __name__)
def record():
    userpath = "userfiles/%s.txt" % session['username']
    #session['guesses'] is a list of words in the form of :c1r2a0n1e2; 0 -> gray, 1 -> yellow, 2 -> green
    with open (userpath, "r+") as userfile:
        len = session['guesses'].length()
        userfile.write(date.today().strftime("%m/%d/%y"), "\n")
        for i in range(len):
            userfile.write(session['guesses'][i], "|")
        userfile.write("\n")


@bp.route("/history", methods=['GET', 'POST'])
def getHistory():
    history = []
    userpath = "userfiles/%s.txt" % session['username']
    with open (userpath, "r+") as userfile:
        lines = userfile.readlines()
        for line in lines:
            if "/" in lines:
                date_history = []
                date_history.append(line)
            else:
                len = length(line)
                word = ''
                for i in range(0, len, 2):
                    word += line[i]
                date_history.append(line)
            if lines == "\n":
                history.append(date_history)
    return render_template("history.html", matches=history)
