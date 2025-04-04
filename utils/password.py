from random import SystemRandom
from string import ascii_letters
from typing import Optional, Tuple
from hashlib import pbkdf2_hmac

HASH_ITERATIONS = 10_000 
LETTERS = list(ascii_letters)

def generate_salt(length: int = 16) -> str:
    """
    Generates a salt for hashing passwords
    Returns a string of `length` random characters
    in the range [a-z, A-Z, 0-9].
    """
    salt = ""
    sys_random = SystemRandom()
    for _ in range(length):
        salt += sys_random.choice(LETTERS)
    return salt

def hash_password(password: str, salt: Optional[str] = None) -> Tuple[int, str]:
    """
    Generates a password hash
    Returns an integer, the hash of the password
    """
    if salt is None:
        salt = generate_salt()
    hash = pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt.encode(),
        HASH_ITERATIONS
    )
    # Convert hash to int
    hash = int(hash.hex(), 16)
    return hash, salt

def validate_password(new_password: str, hash: int, salt: str) -> bool:
    """
    Validate if the password provided matches the hash
    Returns a boolean
    """
    new_hash = pbkdf2_hmac(
        'sha256',
        new_password.encode(),
        salt.encode(),
        HASH_ITERATIONS
    )
    # Convert hash to int
    new_hash = int(new_hash.hex(), 16)
    return hash == new_hash


# The below code is used for local testing purposes.
if __name__ == "__main__":
    print("Running tests...")
    password = "this i5 @ prett_ l0nG P@55w0rd!"
    hash, salt = hash_password(password)
    assert(validate_password("well this is a wrong password", hash, salt) == False)
    assert(validate_password(password, hash, salt) == True)
    print("Tests passed!")
