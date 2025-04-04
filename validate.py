def validate_email(email):
    if email.count('@') != 1:
        return False
    if ' ' in email:
        return False
    name, domain = email.split('@')
    if '.' not in domain:
        return False
    
    return True

def validate_password(password):
    if ' ' in password:
        return False
    if len(password) < 12:
        return False
    if password.lower() == password:
        return False
    contains_number = False
    contains_symbol = False
    for char in password:
        if char in '0123456789':
            contains_number = True
        if char in '!@#$%^&*()-=_+[]\\{}|;\':",./<>?':
            contains_symbol = True
    if not contains_number:
        return False
    if not contains_symbol:
        return False
      
    return True