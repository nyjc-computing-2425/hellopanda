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

DELETE_TABLE_ACCOUNT = """
        DROP TABLE IF EXISTS account
    """

INSERT_INTO_ACCOUNT = """
        INSERT INTO account (email, salt, password, type, name, class, graduation_year)
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

