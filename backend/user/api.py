from ninja.security import HttpBasicAuth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import path
from ninja import Router

from .models import User
from .schemas.login_schema import Credentials, Error, UserSchema

router = Router()

@router.post("/login", response = {401: Error, 200: UserSchema})
def login(request, credentials: Credentials):
    user_credentials = credentials

    user = authenticate(request, username=credentials.username, password=credentials.password)

    if user is not None:
        auth_login(request, user)
        return 200, user
    else:
        return 401, {'message': 'invalid credentials'}


@router.post("/logout")
def logout(request):
    auth_logout(request)
    return {'message': 'logged out'}
