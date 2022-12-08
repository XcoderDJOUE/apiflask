from apiflask import Schema
from apiflask.fields import String

class Users(Schema):
    email = String()
    password = String()
