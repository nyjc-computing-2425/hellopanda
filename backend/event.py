from .base import execute_query
import datetime

from . import sql

####################################EVENT##########################################
def create_event_table():
    """
    Creates the account table
    """
    execute_query(sql.CREATE_TABLE_EVENTS) # type: ignore

#Delete account table
def delete_event_table():
    execute_query(sql.DELETE_TABLE_EVENT)

# Function to store event data
def store_event_data(event_id, start, end, topic, synopsis, venue, organiser_email) -> None:
    """
    Stores event data

    Parameters
    -------------
    event_id: int
        The id of the event

    start: int
        The starting date of event

    end: int
        The end

    topic: str
        The topic of the event

    synopsis: str
        brief summary of even

    venue: str
        The venue of event

    organiser_email: str
        The email of the organiser
          
    """
    execute_query(sql.INSERT_INTO_EVENT,
        [event_id, start, end, topic, synopsis, venue, organiser_email])

#Functions to retrieve data
def retrieve_byname(name):
    return execute_query(sql.RETRIEVE_EVENT_BYNAME,[name])

def retrieve_byorganiser(organiser_email):
    return execute_query(sql.RETRIEVE_EVENT_BYORGANISER,[organiser_email])

#Functions to update event data
def update_start(event_id, start):
    execute_query(sql.UPDATE_EVENT_START, [start, event_id])

def update_end(event_id, end):
    execute_query(sql.UPDATE_EVENT_END, [end, event_id])

def update_topic(event_id, topic):
    execute_query(sql.UPDATE_EVENT_TOPIC, [topic, event_id])
    
def update_synopsis(event_id, synopsis):
    execute_query(sql.UPDATE_EVENT_SYNOPSIS, [synopsis, event_id])

def update_venue(event_id, venue):
    execute_query(sql.UPDATE_EVENT_VENUE, [venue, event_id])

#Function to return list of all events
def retrieve_all_events():
        return execute_query(sql.RETRIEVE_ALL_EVENTS)

def retrieve_current_events():
    x = str(datetime.datetime.now())
    x = x[:19]

    return execute_query(sql.RETRIEVE_CURRENT_EVENTS,[x, x])


def retrieve_upcoming_events():
    x = str(datetime.datetime.now())
    x = x[:19]

    return execute_query(sql.RETRIEVE_UPCOMING_EVENTS,[x]   )

#Functions to download event data
def participants_to_csv(event_id, filename):
    """
    Converts the participants of an event to a CSV format
    """
    participants = execute_query(sql.GET_EVENT_PARTICIPATION, [event_id])
    csv_data = "Email, Attendance\n"
    for participant in participants:
        csv_data += f"{participant['email']}, {participant['attendance']}\n"
    
    with open(filename, "w") as f:
        f.write(csv_data)
    return True

