from flask import Flask, render_template, Markup
import numpy as np

app = Flask(__name__, static_url_path='/templates')

@app.route("/")

def home():
    return render_template('hackathon.html')

def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()