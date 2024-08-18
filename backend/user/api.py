from ninja.security import HttpBasicAuth
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import path
from ninja import Router

from .models import User
from .schemas.login_schema import Credentials

router = Router()

@router.post("/login")
def login(request, credentials: Credentials):
    user_credentials = credentials

    user = authenticate(request, username=user_credentials.username, password=user_credentials.password)

    if user is not None:
        auth_login(request._request, user)
        serializer = UserSerializer(user, many=False)
        return serializer.data
    else:
        return {'message': 'invalid credentials'}


@router.post("/logout")
def logout(request):
    auth_logout(request)
    return {'message': 'logged out'}
