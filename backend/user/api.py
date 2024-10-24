from ninja.security import HttpBasicAuth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import path
from ninja import Router

from .models import User
from .schemas.error_schema import Error
from .schemas.login_schema import Credentials, UserSchema
from .schemas.signup_schema import SignupSchema

from ninja.security import django_auth

router = Router(auth=django_auth)

@router.get("/", response = {200: list[UserSchema]})
def list(request):
    return User.objects.all()

@router.post("/login", response = {401: Error, 200: UserSchema}, auth=None)
def login(request, credentials: Credentials):
    user = authenticate(request, email=credentials.email, password=credentials.password)

    if user is not None:
        auth_login(request, user)
        return 200, user
    else:
        return 401, {'message': 'invalid credentials'}


@router.post("/signup", response = {422: Error, 201: UserSchema}, auth=None)
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
        return 401, {'message': 'error creating user'}


@router.post("/logout")
def logout(request):
    auth_logout(request)
    return {'message': 'logged out'}
