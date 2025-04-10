from flask import Flask, abort, redirect, render_template

app = Flask(__name__)


@app.route('/') # Sprint 2 / MVP
def index(): 
    return render_template("pages/index.html")
    

@app.route('/student') # Sprint 2 / MVP
def student_page():
    return render_template('student.html')
    

@app.route('/student/event_details')
def student_event_details_page():
    return render_template("studenteventdetails.html")
    

@app.route('/login') # Sprint 2 / MVP
def login_page():
    return render_template('login.html')


@app.route('/organiser')
def organiser_page():
    return "organiser home page"


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

