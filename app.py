from flask import Flask, render_template

app = Flask(__name__, template_folder='src')

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("index.html")

