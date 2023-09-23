import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
e#nv_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
#app.config.from_object(env_config)
#secret_key = app.config.get("SECRET_KEY")


@app.get("/")
def home_get():
    return render_template("index.html")

@app.post("/")
def home_post():
    return render_template("index.html")


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

@app.route("/about")
def about():
    return render_template("index.html")

