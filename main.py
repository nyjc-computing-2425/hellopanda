from flask import Flask, abort, redirect, render_template

app = Flask(__name__)

#temp func
def get_events():
    return [{"id": "brawl", "topic": "brawl stars"}, 
            {"id": "nbd", "topic": "no bag day"}]

@app.route('/') # Sprint 2 / MVP
def index(): 
    return render_template("pages/index/index.html")
    

@app.route('/student') # Sprint 2 / MVP
def student_page():
     # TODO: 
    # 1. Get function from backend to get all events
    # 2. Pass this data to render template
     # (Optional) Create placeholder data on our end and pass it to render_template for testing
    
    events = get_events()
    return render_template('pages/student/student.html', events = events)

@app.route('/login') # Sprint 2 / MVP
def login_page():
    return render_template('pages/login/login.html')


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
    app.run(host='0.0.0.0', port=5001, debug=True)

