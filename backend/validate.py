from . import account
from . import password as pwd

def email(email_):
    if email_.count('@') != 1:
        return False
    if ' ' in email_:
        return False
    name, domain = email_.split('@')
    if '.' not in domain:
        return False
    
    return True

def password(password_):
    if ' ' in password_:
        return False
    if len(password_) < 12:
        return False
    if password_.lower() == password_:
        return False
    contains_number = False
    contains_symbol = False
    for char in password_:
        if char in '0123456789':
            contains_number = True
        if char in '!@#$%^&*()-=_+[]\\{}|;\':",./<>?':
            contains_symbol = True
    if not contains_number:
        return False
    if not contains_symbol:
        return False
      
    return True

def name(name_):
    for char in name_:
        if char in '0123456789':
            return False
        if char in '!@#$%^&*()=_+[]\\{}|;\':",./<>?':
            return False
        
    return True

def class_number(class_):
    if len(class_) != 4:
        return False
    for char in class_:
        if char not in '0123456789':
            return False
        
    return True



def authenticate(username: str, password: str) -> bool:
    if not account.check_email(username):
        return False
    data = account.retrieve_byemail(username)[0]
    res = pwd.validate_password(password, data["password"], data["salt"])
    return res

