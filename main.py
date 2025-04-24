import secrets

from flask import Flask, abort, redirect, render_template, request, session


# from validate import authenticate
from backend.__init__ import acc_type, validate
from backend.event import retrieve_byname
from backend.signup import add_student_to_event, remove_student_from_event

app = Flask(__name__)


@app.route('/') # Sprint 2 / MVP
def index(): 
    return render_template("pages/index/index.html")
    

@app.route('/student') # Sprint 2 / MVP
def student_page():
    return render_template('/pages/student/student.html', events= [{"id":"blm day", "topic":"gimme fried chicken"},
                                                                   {"id":"reverse blm day", "topic":"steal my fried chicken"}])

@app.route('/student/event_details', methods = ["GET", "POST"]) #type: ignore
def student_details_page():
    student_event_details = None
    if request.method == "POST":
        if "signup" in request.form:
            action = request.form["signup"]
            add_student_to_event(user, student_event_details["event_id"]) # type: ignore -> surely login comes before this so we have 'user'
            return render_template('/pages/studenteventdetails/studenteventdetails.html', event = student_event_details, misc_msg="Signed up successfully!") #type: ignore
    
        if "unregister" in request.form:
            action = request.form["unregister"]
            remove_student_from_event(user, student_event_details["event_id"]) # type: ignore -> surely login comes before this so we have 'user'
            return render_template('/pages/studenteventdetails/studenteventdetails.html', event = student_event_details, misc_msg="Unregistered successfully!") #type: ignore
        
        if "what_event" in request.form:
            event_topic = request.form["what_event"]
            student_event_details = retrieve_byname(event_topic)
            return render_template('/pages/studenteventdetails/studenteventdetails.html', event = student_event_details) #type: ignore

        else:
            return redirect("/student")

    elif request.method == "GET":
        return render_template('/pages/studenteventdetails/studenteventdetails.html', event = student_event_details) #type: ignore

@app.route('/login', methods = ["GET", "POST"]) # Sprint 2 / MVP
def login_page():
    if request.method == "GET":
        return render_template('pages/login/login.html')
    else:
        user = request.form["username"]
        pw = request.form["password"]


        # authenticated = False
        # authenticate() is not built yet
        authenticated = validate.authenticate(user, pw)
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

@app.route('/organiser/create_event', methods = ["GET", "POST"]) # Sprint 2 / MVP
def organiser_create_event_page():
    if request.method == "GET":
        return render_template('pages/create_event/create_event.html')
    else:
        
        return render_template('pages/login/login.html')
        

@app.route('/organiser')
def organiser_page():
    return render_template("pages/organiser/organiser.html", events=[{"id":"ny fiesta", "topic":"throw pch into the water"},
                                                                     {"id":"sigma day", "topic":"chicken jockey"}])


@app.route('/organiser/events')
def organiser_events_page():
    return render_template('/pages/organiser-events/organiser-events.html', event = None)


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

