"""sql.py

Module for SQL queries.
"""

CREATE_TABLE_ACCOUNT = """
        CREATE TABLE IF NOT EXISTS "account" (
            "email" TEXT NOT NULL,
            "salt" TEXT NOT NULL,
            "password" TEXT NOT NULL,
            "_type" TEXT NOT NULL,
            "name" TEXT NOT NULL,
            "_class" INTEGER,
            "graduation_year" INTEGER,
            PRIMARY KEY("email")
        );
    """

DELETE_TABLE_ACCOUNT = """
        DROP TABLE IF EXISTS account
    """

INSERT_INTO_ACCOUNT = """
        INSERT INTO account (email, salt, password, _type, name, _class, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """

RETRIEVE_ACCOUNT_BYNAME = """
        SELECT * FROM account
        WHERE name = ?;
    """

RETRIEVE_ACCOUNT_BYCLASS = """
        SELECT * FROM account
        WHERE _class = ?;
    """

RETRIEVE_ACCOUNT_BYEMAIL = """
        SELECT * FROM account
        WHERE email = ?;
    """

RETRIEVE_ACCOUNT_BYYEAR = """
        SELECT * FROM account
        WHERE year = ?;
    """

UPDATE_ACCOUNT_NAME = """
        UPDATE account
        SET name = ?
        WHERE email = ?;
    """

UPDATE_ACCOUNT_CLASS = """
        UPDATE account
        SET _class = ?
        WHERE email = ?;
    """

UPDATE_ACCOUNT_EMAIL = """
        UPDATE account
        SET email = ?
        WHERE email = ?;
    """

UPDATE_ACCOUNT_YEAR = """
        UPDATE account
        SET graduation_year = ?
        WHERE email = ?; 
    """


#EVENTS
CREATE_TABLE_EVENTS = """
        CREATE TABLE IF NOT EXISTS "event" (
            "event_id" INTEGER NOT NULL,
            "start_datetime" TEXT NOT NULL,
            "end_datetime" TEXT NOT NULL,
            "topic" TEXT NOT NULL,
            "synopsis" TEXT NOT NULL,
            "venue" TEXT,
            PRIMARY KEY("event_id")
        );
    """

DELETE_TABLE_EVENT = """
        DROP TABLE IF EXISTS event
    """

INSERT_INTO_EVENT = """
        INSERT INTO event (event_id, start_datetime, end_datetime, topic, synopsis, venue)
        VALUES (?, ?, ?, ?, ?, ?)
    """

UPDATE_EVENT_START = """UPDATE event 
        SET start_datetime = ?
        WHERE event_id = ?
    """

UPDATE_EVENT_END = """UPDATE event 
        SET end_datetime = ?
        WHERE event_id = ?
    """

UPDATE_EVENT_TOPIC = """UPDATE event 
        SET topic = ?
        WHERE event_id = ?
    """

UPDATE_EVENT_SYNOPSIS = """UPDATE event 
        SET synopsis = ?
        WHERE event_id = ?
    """

UPDATE_EVENT_VENUE = """UPDATE event 
        SET venue = ?
        WHERE ievent_idd = ?
    """
RETRIEVE_ALL_EVENTS = """
        SELECT *
        FROM event;
    """

RETRIEVE_EVENT_BYNAME = """
        SELECT *
        FROM event
        WHERE topic=?
    """

RETRIEVE_CURRENT_EVENTS = """
        SELECT *
        FROM event
        WHERE (start_datetime<=? AND end_datetime>=?)
    """

RETRIEVE_UPCOMING_EVENTS = """
        SELECT *
        FROM event
        WHERE (start_datetime>?)
    """

CREATE_TABLE_SIGNUP = """
        CREATE TABLE IF NOT EXISTS "signup" (
            "email" TEXT NOT NULL,
            "event_id" INTEGER NOT NULL,
            "attendance" INTEGER DEFAULT 0
        );
    """

DELETE_SIGNUP_TABLE = """
        DROP TABLE IF EXISTS signup;
    """

GET_SIGN_UP_EVENT = """
        SELECT *
        FROM signup
        WHERE email = ?
    """

ADD_STUDENT_TO_EVENT = """
        INSERT INTO signup
        VALUES (?, ?, ?)
    """

REMOVE_STUDENT_FROM_EVENT = """
        DELETE FROM signup 
        WHERE email = ? AND event_id = ?
    """

GET_EVENT_PARTICIPATION = """
        SELECT * FROM signup 
        WHERE event_id = ?;
    """

MARK_ATTENDENCE = """
        UPDATE signup SET "attendance" = ?
        WHERE email = ? AND event_id = ?    
    """

IS_PRESENT ="""
        SELECT "attendance" FROM signup
        WHERE email = ? AND event_id = ?
        
    """
