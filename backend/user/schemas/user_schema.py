from ninja import Schema
from typing import Optional

class UserSchema(Schema):
    email: str
    first_name: str
    last_name: str


class UserCreateSchema(Schema):
    email: str
    first_name: str
    last_name: str
    password: str


class UserUpdateSchema(Schema):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None