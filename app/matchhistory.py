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
    #session['guesses'] is a list of words in the form of :c1r2a0n1e2; 0 -> green 1 - yellow 2 gray
    with open (userpath, "r+") as userfile:
        len = session['game']['guesses'].length()
        userfile.write(date.today().strftime("%m/%d/%y"), len, "\n")
        for i in range(len):
            userfile.write(session['game']['guesses'][i], "|")
        for i in range(len):
            for i in range(5):
                userfile.write(session['game']['colors'][i], ",")
        userfile.write("\n")

#Guesses, Date, GuessCount, colors

@bp.route("/history", methods=['GET', 'POST'])
def getHistory():
    if request.method == "GET":
        history = []
        chistory = []
        guesscount = []
        date_history = []
        userpath = "userfiles/%s.txt" % session['username']
        with open (userpath, "r+") as userfile:
            lines = userfile.readlines()
            for line in lines:
                if "/" in line:
                    c = []
                    date_history.append(line.rstrip("\n"))
                if "|" in line:
                    words = line.split('|')
                    print(words)
                    for word in words:
                        date_history.append(word.rstrip("\n"))
                if "," in line:
                    colors = line.rstrip("\n").split(',')
                    for color in colors:
                        c.append(color)
                if line.isdigit():
                    guesscount.append(line.rstrip("\n"))
                if line == "\n":
                    print('yes')
                    chistory.append(c)
                    history.append(date_history)
        print(guesscount)
        return render_template("history.html", dates=date_history, matches=history, guesscolors=chistory, count=guesscount)
