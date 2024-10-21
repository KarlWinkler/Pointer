from ninja import Schema

class Credentials(Schema):
    email: str
    password: str

class UserSchema(Schema):
    email: str
    first_name: str
    last_name: str
