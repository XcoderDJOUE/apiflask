import random
from datetime import datetime, timedelta
import re
from passlib.context import CryptContext
crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generateverificationcode():
    return random.randrange(1111, 9999)

def addmin(value : int):
    now = datetime.today()
    result_3 = now + timedelta(minutes=value)
    return result_3

def valid_email(email: str):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,}$", email))

def passwordencode(password: str):
    hashval = crypt.hash(password)
    return hashval

def passwordecode(password: str, hash: str):
    hashvaldecoded = crypt.verify(password, hash)
    return hashvaldecoded

def dateverify(dbdate: None):
    now = datetime.today()
    today = now.timestamp()
    if int(today) > int(dbdate):
        return False
    else:
        return True

"""sendemail simulation

Keyword arguments: email, code
email: email of client, code: code verification of user email
Return: simulation to send code of confirmation in client email
"""

def sendemail(email: str, code: int):
    print('--------------------------------------------------------------')
    print(f'email sent with activation code {code} to {email}')
    print('--------------------------------------------------------------')