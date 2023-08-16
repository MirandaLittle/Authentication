import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    render_template("login.html", title="Login")
    error = None
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        password = request.form["password"]
        hashed_password = hash_password(password)
        if hashed_password == get_users()[username]:
            return redirect(url_for("dashboard"))
    else: 
        return render_template("login.html", title="Login", error=True)
    

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        username = session["user"]
        return render_template("dashboard.html", user=username)
    else: 
        return redirect(url_for("login", error=True))
    


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

