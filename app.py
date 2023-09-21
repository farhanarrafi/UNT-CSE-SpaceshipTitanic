import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='src')
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
secret_key = app.config.get("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("index.html")

