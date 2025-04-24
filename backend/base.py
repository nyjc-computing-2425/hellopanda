import sqlite3

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


