"""sql.py

Module for SQL queries.
"""

CREATE_TABLE_ACCOUNT = """
        CREATE TABLE IF NOT EXISTS "account" (
            "email" TEXT NOT NULL,
            "salt" TEXT NOT NULL,
            "password" INTEGER NOT NULL,
            "type" TEXT NOT NULL,
            "name" TEXT NOT NULL,
            "class" INTEGER,
            "graduation_year" INTEGER,
            PRIMARY KEY("email")
        );
    """