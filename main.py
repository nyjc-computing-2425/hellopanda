from flask import Flask, abort, redirect, render_template, request
from validate import *

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/home")


@app.route('/home')
def home_page():
    return "home page"


@app.route('/student')
def student_page():
    return "student page"


@app.route('/student/event_details')
def student_event_details_page():
    return "student event details page"


@app.route('/login', methods=["GET", "POST"])
def login_page():
    if request.method == "GET":
        return render_template("pages/login.html")
    elif request.method == "POST":
        if not email(request.form["email"]) or not password(request.form["password"]):
            return render_template("pages/login.html", errormsg = "login unsuccessful")
        return render_template("pages/login.html")
    return redirect("/home")

@app.route('/organiser')
def organiser_page():
    return "organiser home page"


@app.route('/organiser/events')
def organiser_events_page():
    return "organiser events page"


@app.route('/organiser/create_event')
def organiser_create_event_page():
    return "organiser create event page" 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

