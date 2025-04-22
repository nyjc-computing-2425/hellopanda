from .base import execute_query

####################################SIGNUP#################################
def create_signup_table() -> None:
    """
    Creates the account table
    """
    execute_query("""
        CREATE TABLE IF NOT EXISTS "signup" (
            "email" TEXT NOT NULL,
            "event_id" INTEGER NOT NULL
        );
    """)

#Delete account table
def delete_signup_table():
    execute_query("""
        DROP TABLE IF EXISTS signup;
    """)

#retrieve events signed up
def get_signed_up_events(email):
    return execute_query("""
        SELECT *
        FROM signup
        WHERE email = ?
""", [email])

def add_student_to_event(email, event_id):
    execute_query("""
        INSERT INTO signup
        VALUES (email,event_id)
        """)
def remove_student_from_event(email, event_id):
    execute_query("""
        DELETE FROM signup 
        WHERE email = ? AND event_id = ?
        """)
