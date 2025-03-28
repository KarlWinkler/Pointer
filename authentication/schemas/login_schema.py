from ninja import Schema

class Credentials(Schema):
    email: str
    password: str
