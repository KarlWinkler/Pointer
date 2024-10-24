from ninja import Schema

class UserSchema(Schema):
    email: str
    first_name: str
    last_name: str


class UserCreateSchema(Schema):
    email: str
    first_name: str
    last_name: str
    password: str