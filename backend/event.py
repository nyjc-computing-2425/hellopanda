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
def store_event_data(id, start, end, topic, synopsis, venue) -> None:
    """
    Stores event data

    Parameters
    -------------
    id: int
        The id of the student

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
          
    """
    execute_query(sql.INSERT_INTO_EVENT,
        [id, start, end, topic, synopsis, venue])

#Functions to update event data
def update_start(id, start):
    execute_query(sql.UPDATE_EVENT_START, [start, id])

def update_end(id, end):
    execute_query(sql.UPDATE_EVENT_END, [end, id])

def update_topic(id, topic):
    execute_query(sql.UPDATE_EVENT_TOPIC, [topic, id])
    
def update_synopsis(id, synopsis):
    execute_query(sql.UPDATE_EVENT_SYNOPSIS, [synopsis, id])

def update_venue(id, venue):
    execute_query(sql.UPDATE_EVENT_VENUE, [venue, id])

#Function to return list of all events
def retrieve_event():
        return execute_query(sql.RETRIEVE_EVENT)

def retrieve_current_event():
    now = datetime.datetime.today()
    events = retrieve_event()
    lst = []
    if events:
        for dic in events:
            start = dic['start_datetime']
            end = dic['end_datetime']
            if start <= now <= end:
                lst.append(dic)
    return lst


def retrieve_upcoming_event():
    x = str(datetime.datetime.now())
    x = x[:19]

    return execute_query("""
        SELECT *
        FROM event
        WHERE (start_datetime>x)
"""    )

