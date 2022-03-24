from flask import g
import sqlite3

DB_FILE="database.db"

create_users = '''CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                hash TEXT,
                userfile TEXT
                lastplayed TEXT)'''


def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    d = get_db()
    c = d.cursor()
    c.execute(create_users)
    d.commit()
