from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from cs50 import SQL

from helpers import login_required, apology

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

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///rpg_tools.db")

# Default landing page, after logged in
@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():

    # When user tries to submit form
    if request.method == "POST":

        # Check to see if username already exists
        rows = db.execute("SELECT username FROM users WHERE username = :username", username=request.form.get('user'))

        # If it does, error message!
        if len(rows) > 0:
           return apology("Username already exists", 403)

        # If not, put them in the database
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", 
                       username=request.form.get('user'), hash=generate_password_hash(request.form.get('pwd'), 
                                                                      method='pbkdf2:sha256', salt_length=8))
        
        return render_template("/login.html")

    # When user navigates to page
    else:
        return render_template("register.html")


@app.route("/dice")
def dice():
    # Javascript dice roller
    return render_template("dice.html")

@app.route("/hp")
@login_required
def hp():
    if request.method == 'GET':
        userid = session['user_id']
        characters = db.execute("SELECT name FROM characters WHERE user_id = :id", id = userid)
        if characters == None:
            print("no characters for this user")
            return render_template("hp.html", characters = characters)
        else:
            return render_template("hp.html", characters=characters)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        userid = session['user_id']
        addcharname = request.form.get('addcharname')
        maxhp = request.form.get('maxhp')
        if addcharname != "":
            db.execute("INSERT INTO characters (name, current, max, user_id) VALUES (:charname, :current, :maxhp, :userid)", 
                    charname=addcharname, current=maxhp, maxhp=maxhp, userid=userid) 
            return redirect("/hp")
        else:
            return redirect("/hp")
@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    if request.method == 'GET':
        userid = session['user_id']
        characters = db.execute("SELECT name FROM characters WHERE user_id =:id", id = userid)
        return render_template("remove.html", characters=characters)
    else:
        userid = session['user_id']
        removecharname = request.form.get('removecharname')
        return redirect("/hp")
