from flask import Flask, render_template
from . import templates

app= Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def create_app():
  
    return app


