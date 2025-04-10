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
        SET year = ?
        WHERE email = ?;
    """


#EVENTS
CREATE_TABLE_EVENTS = """
        CREATE TABLE IF NOT EXISTS "account" (
            "id" INTEGER NOT NULL,
            "start_datetime" TEXT NOT NULL,
            "end_datetime" TEXT NOT NULL,
            "topic" TEXT NOT NULL,
            "synopsis" TEXT NOT NULL,
            "venue" TEXT,
            PRIMARY KEY("id")
        );
    """

DELETE_TABLE_EVENT = """
        DROP TABLE IF EXISTS event
    """

INSERT_INTO_EVENT = """
        INSERT INTO event (id, start_datetime, end_datetime, topic, synopsis, venue)
        VALUES (?, ?, ?, ?, ?, ?)
    """

UPDATE_EVENT_START = """UPDATE event 
        SET start_datetime = ?
        WHERE id = ?
    """

UPDATE_EVENT_END = """UPDATE event 
        SET end_datetime = ?
        WHERE id = ?
    """

UPDATE_EVENT_TOPIC = """UPDATE event 
        SET topic = ?
        WHERE id = ?
    """

UPDATE_EVENT_SYNOPSIS = """UPDATE event 
        SET synopsis = ?
        WHERE id = ?
    """

UPDATE_EVENT_VENUE = """UPDATE event 
        SET venue = ?
        WHERE id = ?
    """
RETRIEVE_EVENT = """
        SELECT *
        FROM event;
    """
