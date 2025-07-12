from flask import flask

app=flask(__name__)

@app.route("/info")
def myinfo():
          return "i am rajveer singh"

@app.route("/phone")
def myphone():
          return "9057592503"

app.run(host="0.0.0.0")