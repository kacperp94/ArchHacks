from flask import Flask
import numpy as np


app = Flask(__name__)

@app.route("/")

def home():
    return render_template()

def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run()