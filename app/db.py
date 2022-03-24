from flask import g
import sqlite3
import os

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                hash TEXT,
                userfile TEXT,
                lastplayed TEXT)'''

def init_db():
    DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
    db = sqlite3.connect(DATABASE, check_same_thread=False)
    c = db.cursor()
    c.execute(create_users)
    db.commit()
