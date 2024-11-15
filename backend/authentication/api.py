from ninja.security import HttpBasicAuth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import path
from ninja import Router

from user.models import User
from authentication.schemas.error_schema import Error
from authentication.schemas.login_schema import Credentials
from authentication.schemas.signup_schema import SignupSchema
from user.schemas.user_schema import UserSchema

router = Router()

@router.post("/login", response={401: Error, 200: UserSchema})
def login(request, credentials: Credentials):
    user = authenticate(request, email=credentials.email, password=credentials.password)

    if user is not None:
        auth_login(request, user)
        return 200, user
    else:
        return 401, {'message': 'invalid credentials'}


@router.post("/signup", response={422: Error, 201: UserSchema})
def signup(request, signup: SignupSchema):
    try:
        user = User.objects.create(
            email=signup.email,
            first_name=signup.first_name,
            last_name=signup.last_name
        )
        user.set_password(signup.password)
        user.save()

        return 201, user
    except:
        return 401, {'message': 'Error creating user'}


@router.post("/logout")
def logout(request):
    auth_logout(request)
    return {'message': 'Logged out'}
