import sqlite3

import sql as sql


####################################ACCOUNT#################################
# Create the table
def create_account_table() -> None:
    """
    Creates the account table
    """
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute(sql.CREATE_TABLE_ACCOUNT)

    conn.commit()
    conn.close()

#Delete account table
def delete_account_table():
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    cursor.execute("""
            DROP TABLE IF EXISTS account
        """)
    
    conn.commit()
    conn.close()

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
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO account (email, salt, password, type, name, class, graduation_year)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [email, salt, password, _type, name, _class, graduation_year])

    conn.commit()
    conn.close()



#Functions to retieve account data
def retrieve_byname(name) -> list:
    """
    Returns a list of students with the given name

    Parameters
    -------------
    name: str
        The name of the student to find
        
    Returns
    -------------
    list
        The result of the search
    """
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM account
            WHERE name = ?;
        """,[name])
    result = cursor.fetchall()

    conn.commit()
    conn.close()
    
    return result

def retrieve_byclass(clas):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            SELECT * FROM account
            WHERE _class = ?;
        """,[clas])
    result = cursor.fetchall()

    conn.commit()
    conn.close()
    
    return result

def retrieve_byemail(email):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            SELECT * FROM account
            WHERE email = ?;
        """, 
        [email]
    )
    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result

def retrieve_byyear(year):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            SELECT * FROM account
            WHERE year = ?;
        """,
        [year]
    )
    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result

def acc_type(email: str) -> str:
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM account
            WHERE email = ?;
        """,
        [email]
    )

    return result[0]["_type"] if result else "Email does not exist"

def check_email(email):
    return retrieve_byemail(email)!=[]


#Functions to update account data
def update_name(email, new_name):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            UPDATE account
            SET name = ?
            WHERE email = ?;
        """, [new_name, email])

    conn.commit()
    conn.close()

def update_class(email, new_class):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            UPDATE account
            SET _class = ?
            WHERE email = ?;
        """, [new_class, email])
    
    conn.commit()
    conn.close()

def update_email(email, new_email):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            UPDATE account
            SET email = ?
            WHERE email = ?;
        """, [new_email, email])
    
    conn.commit()
    conn.close()

def update_year(email, new_year):
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    
    cursor.execute("""
            UPDATE account
            SET year = ?
            WHERE email = ?;
        """, [new_year, email])

    conn.commit()
    conn.close()



####################################EVENT##########################################
def create_event_table():
    """
    Creates the account table
    """
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute(sql.CREATE_TABLE_EVENT)

    conn.commit()
    conn.close()

#Delete account table
def delete_event_table():
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()
    cursor.execute("""
            DROP TABLE IF EXISTS event
        """)


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


