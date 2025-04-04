import sqlite3

# Create the table
def create_account_table() -> None:
    """
    Creates the account table
    """
    conn = sqlite3.connect('capstone.db')
    cursor = conn.cursor()

    cursor.execute("""
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
        The account type (admin/student)

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


if __name__ == "__main__":
    create_account_table()
    store_account_data('3', '1', '123', '1', 'John Doe', 101, 2024)
    print(retrieve_byname('John Doe'))
    update_name('3','hehe')
    # update_email('3','4')
    print(retrieve_byname('hehe'))
