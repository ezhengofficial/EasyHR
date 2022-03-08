from flask import Flask, render_template, redirect, request, session
import json
import os
import urllib3
import sqlite3
import time

app = Flask(__name__)
app.secret_key = os.urandom(32)
app.debug = True
app.run()