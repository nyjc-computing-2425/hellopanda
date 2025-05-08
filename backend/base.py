import os
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor

####################################QUERY##################################
def execute_query(query, params=None):
    """
    Executes a SQL query. Automatically returns results for SELECT queries,
    and commits changes for INSERT/UPDATE/DELETE/DDL statements.

    Returns:
        list[dict] if SELECT query, else None
    """
    if os.environ["DB_TYPE"] == "sqlite":
        return execute_sqlite_query(query, params)
    elif os.environ["DB_TYPE"] == "postgres":
        return execute_postgres_query(query, params)


def execute_sqlite_query(query, params=None) -> list[dict]:
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
    except Exception as e:
        raise e
    else:
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        else:
            return []
    finally:
        conn.commit()
        conn.close()


def execute_postgres_query(query, params=None) -> list[dict]:
    """
    Executes a SQL query on a PostgreSQL database. Automatically returns results for SELECT queries,
    and commits changes for INSERT/UPDATE/DELETE/DDL statements.

    Returns:
        list[dict] if SELECT query, else None
    """
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(query, params or [])
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        else:
            return []
    except Exception as e:
        raise e
    finally:
        conn.commit()
        cursor.close()
        conn.close()