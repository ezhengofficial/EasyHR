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
        len = session['game']['guesses'].length()
        userfile.write(date.today().strftime("%m/%d/%y"), "\n")
        for i in range(len):
            userfile.write(session['game']['guesses'][i], "|")
        for i in range(len):
            userfile.write(session['game']['colors'][i], ",")
        userfile.write("\n")


@bp.route("/history", methods=['GET', 'POST'])
def getHistory():
    history = []
    chistory = []
    userpath = "userfiles/%s.txt" % session['username']
    with open (userpath, "r+") as userfile:
        lines = userfile.readlines()
        for line in lines:
            if "/" in line:
                date_history = []
                c = []
                date_history.append(line)
            if "|" in line:
                words = line.split('|')
                for word in words:
                    date_history.append(word)
            if "," in line:
                colors = line.split(',')
                for color in colors:
                    c.append(colors)
            if line == "\n":
                chistory.append(c)
                history.append(date_history)
    return render_template("history.html", matches=history, guesscolors=chistory)
