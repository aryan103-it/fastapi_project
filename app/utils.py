from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash(password: str):
    return password_hash.hash(password)


def verify(plain_pwd, hashed_pwd):
    return password_hash.verify(plain_pwd, hashed_pwd)
