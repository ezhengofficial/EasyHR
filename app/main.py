from flask import Flask, app, render_template, redirect, request

app = Flask(__name__)

        
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
