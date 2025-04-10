import sqlite3

import sql as sql

####################################QUERY##################################
def execute_query(query, params=None) -> list|None:
    """
    Executes a SQL query. Automatically returns results for SELECT queries,
    and commits changes for INSERT/UPDATE/DELETE/DDL statements.

    Returns:
        list[dict] if SELECT query, else None
    """
    conn = sqlite3.connect('capstone.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute(query, params or [])
        
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    except Exception as e:
        print("SQL Error:", e)
        #raise
    finally:
        conn.commit()
        conn.close()


####################################ACCOUNT#################################
# Create the table
def create_account_table() -> None:
    """
    Creates the account table
    """
    execute_query(sql.CREATE_TABLE_ACCOUNT)

#Delete account table
def delete_account_table():
    execute_query("""
            DROP TABLE IF EXISTS account
        """)

# Function to store account data
def store_account_data(email, salt, password, _type, name, _class, graduation_year) -> None:
    """
    Stores account data

    Parameters
    -------------
    email: str
        The email of the student

    salt: str
        The salt for the password

    password: int
        The hashed password

    _type: str
        The account type (student/organiser)

    name: str
        The name of the user

    _class: int or None
        The class of the student. None if user is an admin

    graduation_year: int or None
        The grad year of the student. None if user is an admin
        
    """
    execute_query("""
        INSERT INTO account (email, salt, password, _type, name, _class, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [email, salt, password, _type, name, _class, graduation_year])



#Functions to retieve account data
def retrieve_byname(name):
    """
    Returns a list of students with the given name

    Parameters
    -------------
    name: str
        The name of the student to find
        
    Returns
    -------------
    list
        The result of the search as a list of dictionaries
    """
    return execute_query("""
            SELECT * FROM account
            WHERE name = ?;
        """,[name])

def retrieve_byclass(clas):
    return execute_query("""
            SELECT * FROM account
            WHERE _class = ?;
        """,[clas])
    

def retrieve_byemail(email):

    return execute_query("""
            SELECT * FROM account
            WHERE email = ?;
        """, 
        [email]
    )

def retrieve_byyear(year):
    return execute_query("""
            SELECT * FROM account
            WHERE year = ?;
        """,
        [year]
    )

def acc_type(email: str) -> str:
    result = execute_query("""
            SELECT * FROM account
            WHERE email = ?;
        """,
        [email]
    )

    return result[0]["_type"] if result else "Email does not exist"

#Functions to update account data
def update_name(email, new_name):
    execute_query("""
            UPDATE account
            SET name = ?
            WHERE email = ?;
        """, [new_name, email])

def update_class(email, new_class):
    execute_query("""
            UPDATE account
            SET _class = ?
            WHERE email = ?;
        """, [new_class, email])

def update_email(email, new_email):
    execute_query("""
            UPDATE account
            SET email = ?
            WHERE email = ?;
        """, [new_email, email])
    
def update_year(email, new_year):
    execute_query("""
            UPDATE account
            SET year = ?
            WHERE email = ?;
        """, [new_year, email])



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
