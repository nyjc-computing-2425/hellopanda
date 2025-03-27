from flask import Flask, abort, redirect

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


@app.route('/login')
def login_page():
    return "login page"


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

