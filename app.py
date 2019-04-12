# Code for running the codetrip website on heroku

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def index():
    return render_template('about.html')

@app.route("/portfolio")
def index():
    return render_template('portfolio.html')

@app.route("/contact")
def index():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()
