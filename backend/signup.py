from .base import execute_query
from . import sql

####################################SIGNUP#################################
def create_signup_table() -> None:
    """
    Creates the account table
    """
    execute_query(sql.CREATE_TABLE_SIGNUP)

#Delete account table
def delete_signup_table():
    execute_query(sql.DELETE_SIGNUP_TABLE)

#retrieve events signed up
def get_signed_up_events(email):
    dic = execute_query(sql.GET_SIGN_UP_EVENT, [email])
    return [row["event_id"] for row in dic]

def add_student_to_event(email, event_id):
    execute_query(sql.ADD_STUDENT_TO_EVENT , [email, event_id, False])
    
def remove_student_from_event(email, event_id):
    execute_query(sql.REMOVE_STUDENT_FROM_EVENT, [email, event_id])

def get_event_participants(event_id):
    dic = execute_query(sql.GET_EVENT_PARTICIPATION, [event_id])
    return [row["email"] for row in dic]
