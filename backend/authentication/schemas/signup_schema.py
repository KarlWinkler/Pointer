from ninja import Schema

class SignupSchema(Schema):
  email: str
  first_name: str
  last_name: str
  password: str
