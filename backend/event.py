from .base import execute_query

from . import sql

####################################EVENT##########################################
def create_event_table():
    """
    Creates the account table
    """
    execute_query(sql.CREATE_TABLE_EVENT) # type: ignore

#Delete account table
def delete_event_table():
    execute_query("""
            DROP TABLE IF EXISTS event
        """)

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
    execute_query("""
        INSERT INTO event (id, start_datetime, end_datetime, topic, synopsis, venue)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        [id, start, end, topic, synopsis, venue])

#Functions to update event data
def update_start(id, start):
    execute_query("""UPDATE event 
                  SET start_datetime = ?
                  WHERE id = ?""", [start, id])

def update_end(id, end):
    execute_query("""
            UPDATE event
            SET end_datetime = ?
            WHERE id = ?;
        """, [end, id])

def update_topic(id, topic):
    execute_query("""
            UPDATE event
            SET topic = ?
            WHERE id = ?;
        """, [topic, id])
    
def update_synopsis(id, synopsis):
    execute_query("""
            UPDATE event
            SET synopsis = ?
            WHERE id = ?;
        """, [synopsis, id])

def update_venue(id, venue):
    execute_query("""
            UPDATE event
            SET venue = ?
            WHERE id = ?;
        """, [venue, id])

#Function to return list of all events
def retrieve_event():
        return execute_query("""
            SELECT *
            FROM event;
        """)


if __name__ == "__main__":
    create_account_table()
    #store_account_data("notjohn@gmail.com", "salty", 123, "student", "hehe", 2426, 2025)
    update_class("notjohn@gmail.com", 2426)
    print(acc_type("joh@gmail.com"))
