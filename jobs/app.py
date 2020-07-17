from flask import Flask, render_template 

app = Flask(__name__)

def route(func):
    def inner(url):
        func()
    return inner

@route("/")
@route("/jobs")
def jobs():
    render_template("index.html")
