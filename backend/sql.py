"""sql.py

Module for SQL queries.
"""

CREATE_TABLE_ACCOUNT = """
        CREATE TABLE IF NOT EXISTS "account" (
            "email" TEXT NOT NULL,
            "salt" TEXT NOT NULL,
            "password" INTEGER NOT NULL,
            "_type" TEXT NOT NULL,
            "name" TEXT NOT NULL,
            "_class" INTEGER,
            "graduation_year" INTEGER,
            PRIMARY KEY("email")
        );
    """

CREATE_TABLE_EVENT = """
        CREATE TABLE IF NOT EXISTS "event" (
            "id"	INTEGER NOT NULL,
            "start_datetime"	INTEGER NOT NULL,
            "end_datetime"	INTEGER NOT NULL,
            "topic"	TEXT NOT NULL,
            "synopsis"	TEXT NOT NULL,
            "venue"	TEXT NOT NULL,
            PRIMARY KEY("id")
        );
    """