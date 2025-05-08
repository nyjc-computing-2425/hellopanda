import secrets

from flask import Flask, abort, redirect, render_template, request, session


# from validate import authenticate
from backend.__init__ import acc_type, validate
from backend.event import retrieve_byname, retrieve_all_events
from backend.signup import add_student_to_event, remove_student_from_event
from backend.account import store_account_data
from backend.validate import *
from backend.password import *

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # generate secure key

#global variables to be changed when backend can
def get_user_info():
    isorganiser = False
    logined = False

    uemail = session.get('email', "no email")
    if uemail == "fake stuff": isorganiser = True

    return isorganiser, logined 


@app.route('/') # Sprint 2 / MVP
def index(): 
    isorganiser, logined = get_user_info()
    return render_template("pages/index/index.html", isorganiser=isorganiser, logined=logined)
    

@app.route('/student') # Sprint 2 / MVP
def student_page():
    isorganiser, logined = get_user_info()
    return render_template('/pages/student/student.html', isorganiser=isorganiser , logined=logined, events=retrieve_all_events())

@app.route('/student/event_details', methods = ["GET", "POST"]) #type: ignore
def student_details_page():
    isorganiser, logined = get_user_info()
    student_event_details = retrieve_byname(request.args.get("id"))[0]
    print(request.args.get("id"))
    print(student_event_details)
    if request.method == "POST":
        if "signup" in request.form:
            action = request.form["signup"]
            add_student_to_event(user, student_event_details["event_id"]) # type: ignore -> surely login comes before this so we have 'user'
            return render_template('/pages/studenteventdetails/studenteventdetails.html', logined=logined, isorganiser=isorganiser, event = student_event_details, misc_msg="Signed up successfully!") #type: ignore
    
        if "unregister" in request.form:
            action = request.form["unregister"]
            remove_student_from_event(user, student_event_details["event_id"]) # type: ignore -> surely login comes before this so we have 'user'
            return render_template('/pages/studenteventdetails/studenteventdetails.html', logined=logined, isorganiser=isorganiser, event = student_event_details, misc_msg="Unregistered successfully!") #type: ignore
        
        if "what_event" in request.form:
            event_topic = request.form["what_event"]
            student_event_details = retrieve_byname(event_topic)
            return render_template('/pages/studenteventdetails/studenteventdetails.html', logined=logined, isorganiser=isorganiser, event = student_event_details) #type: ignore

        else:
            return redirect("/student")

    elif request.method == "GET":
        return render_template('/pages/studenteventdetails/studenteventdetails.html', logined=logined, isorganiser=isorganiser, event = student_event_details) #type: ignore
@app.route('/logout')
def logout():
    session.pop(session["user_name"])
    return render_template("/pages/logout/logout.html")
    
@app.route('/login', methods = ["GET", "POST"]) # Sprint 2 / MVP
def login_page():
    isorganiser, logined = get_user_info()
    if request.method == "GET":
        return render_template('pages/login/login.html', logined=logined, isorganiser=isorganiser)
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
                return render_template('pages/login/login.html', logined=logined, isorganiser=isorganiser)
        else:
            return render_template("pages/login/login.html", logined=logined, isorganiser=isorganiser, error_msg = "Login Unsuccessful")

@app.route('/register', methods = ["GET", "POST"])
def register():
    isorganiser, logined = get_user_info()
    if request.method == "GET":
        return render_template("/pages/register/register.html")
    else:
        if not email(request.form["email"]):
            message = "Invalid email"
            return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message=message)
        if not password(request.form["password"]):
            message = "Invalid password"
            return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message=message)
        if not name(request.form["name"]):
            message = "Invalid name"
            return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message=message)
        if not class_number(request.form["class"]):
            message = "Invalid class"
            return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message=message)
        if not request.form["role"]:
            message = "Select a role"
            return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message=message)
        
        # Valid data
     
        hash, salt = hash_password(request.form["password"], generate_salt(4))
        print(request.form["role"])
        store_account_data(request.form["email"], salt, str(hash), request.form["role"], request.form["name"], request.form["class"], None)
        return render_template("/pages/register/register.html", logined=logined, isorganiser=isorganiser, message="Successful!")
    

@app.route('/organiser/create_event', methods = ["GET", "POST"]) # Sprint 2 / MVP
def organiser_create_event_page():
    isorganiser, logined = get_user_info()
    if request.method == "GET":
        return render_template('pages/create_event/create_event.html',logined=logined, isorganiser=isorganiser)
    else:
        
        return render_template('pages/login/login.html', logined=logined, isorganiser=isorganiser)
        

@app.route('/organiser')
def organiser_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/organiser/organiser.html", logined=logined, isorganiser=isorganiser, events=[{"id":"ny fiesta", "topic":"throw pch into the water"},
                                                                     {"id":"sigma day", "topic":"chicken jockey"}])


@app.route('/organiser/events')
def organiser_events_page():
    isorganiser, logined = get_user_info()
    return "organiser events page"



@app.route('/about')
def about_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/about/about.html", logined=logined, isorganiser=isorganiser)

@app.route("/contact")
def contact_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/contact/contact.html",logined=logined, isorganiser=isorganiser)

@app.route("/features")
def features_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/features/features.html", logined=logined, isorganiser=isorganiser)

@app.route("/privacy")
def privacy_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/privacy/privacy.html", logined=logined, isorganiser=isorganiser)
    
@app.route("/terms")
def terms_page():
    isorganiser, logined = get_user_info()
    return render_template("pages/terms/terms.html", logined=logined, isorganiser=isorganiser)

@app.route("/flag.txt")
def flag():
    return "CTFSG{P4NG_P4NG_TH4_G0aT}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)