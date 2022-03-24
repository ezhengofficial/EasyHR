from flask import g
import sqlite3
import os

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                hash TEXT,
                userfile TEXT,
                lastplayed TEXT)'''


def get_db():
    DATABASE = os.path.join(os.path.dirname(__file__), "database.db")
    db = sqlite3.connect(DATABASE, check_same_thread=False, timeout=10)
    return db

def init_db():
    d = get_db()
    c = d.cursor()
    c.execute(create_users)
    d.commit()
