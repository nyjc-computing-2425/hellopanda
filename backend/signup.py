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
    dic = execute_query("""
        SELECT *
        FROM signup
        WHERE email = ?
""", [email])
    return [row["event_id"] for row in dic]

def add_student_to_event(email, event_id):
    execute_query("""
        INSERT INTO signup
        VALUES (?, ?)
        """, [email, event_id])
    
def remove_student_from_event(email, event_id):
    execute_query("""
        DELETE FROM signup 
        WHERE email = ? AND event_id = ?
        """, [email, event_id])

def get_event_participants(event_id):
    dic = execute_query("""
        SELECT * FROM signup 
        WHERE event_id = ?;
        """, [event_id])
    return [row["email"] for row in dic]
