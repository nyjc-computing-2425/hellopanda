import os

if os.environ["DB_TYPE"] == "sqlite":
        placeholder = "?"
else:
        placeholder = "%s"

CREATE_TABLE_ACCOUNT = f"""
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

DELETE_TABLE_ACCOUNT = f"""
        DROP TABLE IF EXISTS account
    """

INSERT_INTO_ACCOUNT = f"""
        INSERT INTO account (email, salt, password, _type, name, _class, graduation_year)
        VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})
    """

RETRIEVE_ACCOUNT_BYNAME = f"""
        SELECT * FROM account
        WHERE name = {placeholder};
    """

RETRIEVE_ACCOUNT_BYCLASS = f"""
        SELECT * FROM account
        WHERE _class = {placeholder};
    """

RETRIEVE_ACCOUNT_BYEMAIL = f"""
        SELECT * FROM account
        WHERE email = {placeholder};
    """

RETRIEVE_ACCOUNT_BYYEAR = f"""
        SELECT * FROM account
        WHERE year = {placeholder};
    """

UPDATE_ACCOUNT_NAME = f"""
        UPDATE account
        SET name = {placeholder}
        WHERE email = {placeholder};
    """

UPDATE_ACCOUNT_CLASS = f"""
        UPDATE account
        SET _class = {placeholder}
        WHERE email = {placeholder};
    """

UPDATE_ACCOUNT_EMAIL = f"""
        UPDATE account
        SET email = {placeholder}
        WHERE email = {placeholder};
    """

UPDATE_ACCOUNT_YEAR = f"""
        UPDATE account
        SET graduation_year = {placeholder}
        WHERE email = {placeholder}; 
    """


#EVENTS
CREATE_TABLE_EVENTS = f"""
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

DELETE_TABLE_EVENT = f"""
        DROP TABLE IF EXISTS event
    """

INSERT_INTO_EVENT = f"""
        INSERT INTO event (event_id, start_datetime, end_datetime, topic, synopsis, venue)
        VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})
    """

UPDATE_EVENT_START = f"""UPDATE event 
        SET start_datetime = {placeholder}
        WHERE event_id = {placeholder}
    """

UPDATE_EVENT_END = f"""UPDATE event 
        SET end_datetime = {placeholder}
        WHERE event_id = {placeholder}
    """

UPDATE_EVENT_TOPIC = f"""UPDATE event 
        SET topic = {placeholder}
        WHERE event_id = {placeholder}
    """

UPDATE_EVENT_SYNOPSIS = f"""UPDATE event 
        SET synopsis = {placeholder}
        WHERE event_id = {placeholder}
    """

UPDATE_EVENT_VENUE = f"""UPDATE event 
        SET venue = {placeholder}
        WHERE ievent_idd = {placeholder}
    """
RETRIEVE_ALL_EVENTS = f"""
        SELECT *
        FROM event;
    """

RETRIEVE_EVENT_BYNAME = f"""
        SELECT *
        FROM event
        WHERE topic={placeholder}
    """

RETRIEVE_CURRENT_EVENTS = f"""
        SELECT *
        FROM event
        WHERE (start_datetime<={placeholder} AND end_datetime>={placeholder})
    """

RETRIEVE_UPCOMING_EVENTS = f"""
        SELECT *
        FROM event
        WHERE (start_datetime>{placeholder})
    """

CREATE_TABLE_SIGNUP = f"""
        CREATE TABLE IF NOT EXISTS "signup" (
            "email" TEXT NOT NULL,
            "event_id" INTEGER NOT NULL,
            "attendance" INTEGER DEFAULT 0
        );
    """

DELETE_SIGNUP_TABLE = f"""
        DROP TABLE IF EXISTS signup;
    """

GET_SIGN_UP_EVENT = f"""
        SELECT *
        FROM signup
        WHERE email = {placeholder}
    """

ADD_STUDENT_TO_EVENT = f"""
        INSERT INTO signup (email, event_id)
        VALUES ({placeholder}, {placeholder}) 
    """

REMOVE_STUDENT_FROM_EVENT = f"""
        DELETE FROM signup 
        WHERE email = {placeholder} AND event_id = {placeholder}
    """

GET_EVENT_PARTICIPATION = f"""
        SELECT * FROM signup 
        WHERE event_id = {placeholder};
    """

MARK_ATTENDENCE = f"""
        UPDATE signup SET "attendance" = {placeholder}
        WHERE email = {placeholder} AND event_id = {placeholder}    
    """

IS_PRESENT ="""
        SELECT "attendance" FROM signup
        WHERE email = {placeholder} AND event_id = {placeholder}
        
    """
