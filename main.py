import secrets

from flask import Flask, abort, redirect, render_template, request, session


# from validate import authenticate
from backend.__init__ import acc_type

app = Flask(__name__)


@app.route('/') # Sprint 2 / MVP
def index(): 
    return render_template("pages/index/index.html")
    

@app.route('/student') # Sprint 2 / MVP
def student_page():
    return render_template('/pages/student/student.html', events= [{"id":"blm day", "topic":"gimme fried chicken"},
                                                                   {"id":"reverse blm day", "topic":"steal my fried chicken"}])

@app.route('/login', methods = ["GET", "POST"]) # Sprint 2 / MVP
def login_page():
    if request.method == "GET":
        return render_template('pages/login/login.html')
    else:
        user = request.form["username"]
        pw = request.form["password"]


        authenticated = False
        # authenticate() is not built yet
        # authenticated = authenticate(user, pw)
        account = acc_type(user)
        if authenticated:
            session["user_name"] = user
            session["password"] = pw
            if account == "student":
                return redirect("/student")
            elif account == "organiser":
                return redirect("/organiser")
            else:
                return render_template('pages/login/login.html')
        else:
            return render_template("pages/login/login.html", error_msg = "Login Unsuccessful")

@app.route('/register')
def register():
    return render_template("/pages/register/register.html")


@app.route('/organiser')
def organiser_page():
    return render_template("pages/organiser/organiser.html", events=[{"id":"ny fiesta", "topic":"throw pch into the water"},
                                                                     {"id":"sigma day", "topic":"chicken jockey"}])


@app.route('/organiser/events')
def organiser_events_page():
    return "organiser events page"


@app.route('/organiser/create_event')
def organiser_create_event_page():
    return "organiser create event page" 

@app.route('/about')
def about_page():
    return render_template("pages/about/about.html")

@app.route("/contact")
def contact_page():
    return render_template("pages/contact/contact.html")

@app.route("/features")
def features_page():
    return render_template("pages/features/features.html")

@app.route("/privacy")
def privacy_page():
    return render_template("pages/privacy/privacy.html")
    
@app.route("/terms")
def terms_page():
    return render_template("pages/terms/terms.html")

@app.route("/flag.txt")
def flag():
    return "CTFSG{P4NG_P4NG_TH4_G0aT}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

