from ninja import Schema

class Credentials(Schema):
    username: str
    password: str

class UserSchema(Schema):
    username: str
    first_name: str
    last_name: str
