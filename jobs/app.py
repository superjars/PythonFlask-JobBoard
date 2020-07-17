from flask import Flask, render_template 

app = Flask(__name__)

@route("/")
@route("/jobs")
def jobs():
    render_template(index.html)