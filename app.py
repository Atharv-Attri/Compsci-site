from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

import email
import text
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/what-is-it")
def what():
    info = text.what_text()
    return render_template("what.html", source=info["source"], text=info["text"])


@app.route("/why-care")
def why():
    info = text.why_text()
    return render_template("why.html", source=info["source"], text=info["text"])


@app.route("/how-help")
def how():
    info = text.how_text()
    return render_template("how.html", source=info["source"], text=info["text"])


@app.route("/pledge", methods=["GET", "POST"])
def pledge():
    if request.method == "GET":
        return render_template("pledge.html")

    toaddr = request.form.get("email")
    email.send(toaddr)
