from flask import Flask, render_template, Markup
import numpy as np

app = Flask(__name__)

@app.route("/")

def home():
    return render_template('hackathon.html')

def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()