from .base import execute_query

from . import sql

####################################ACCOUNT#################################
# Create the table
def create_account_table() -> None:
    """
    Creates the account table
    """
    execute_query(sql.CREATE_TABLE_ACCOUNT)

#Delete account table
def delete_account_table():
    execute_query(sql.DELETE_TABLE_ACCOUNT)

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
    execute_query(sql.INSERT_INTO_ACCOUNT,
        [email, salt, password, _type, name, _class, graduation_year])



#Functions to retieve account data
def retrieve_byname(name):
    """
    Returns a list of students with the given name

    Parameters
    -------------
    name: str
        The name of the student to find
        
    Returns
    -------------
    list
        The result of the search as a list of dictionaries
    """
    return execute_query(sql.RETRIEVE_ACCOUNT_BYNAME,[name])

def retrieve_byclass(clas):
    return execute_query(sql.RETRIEVE_ACCOUNT_BYCLASS,[clas])
    

def retrieve_byemail(email):

    return execute_query(sql.RETRIEVE_ACCOUNT_BYEMAIL, 
        [email]
    )

def retrieve_byyear(year):
    return execute_query(sql.RETRIEVE_ACCOUNT_BYYEAR,
        [year]
    )

def acc_type(email: str) -> str:
    result = execute_query(sql.RETRIEVE_ACCOUNT_BYEMAIL,
        [email]
    )

    return result[0]["_type"] if result else "Email does not exist"

#Functions to update account data
def update_name(email, new_name):
    execute_query(sql.UPDATE_ACCOUNT_NAME, [new_name, email])

def update_class(email, new_class):
    execute_query(sql.UPDATE_ACCOUNT_CLASS, [new_class, email])

def update_email(email, new_email):
    execute_query(sql.UPDATE_ACCOUNT_EMAIL, [new_email, email])
    
def update_year(email, new_year):
    execute_query(sql.UPDATE_ACCOUNT_YEAR, [new_year, email])

def check_email(email):
    if retrieve_byemail(email) == []:
        return False
    else:
        return True
