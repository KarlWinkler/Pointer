from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import Router

from .models import User
from .schemas.error_schema import Error
from .schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema

from ninja.security import django_auth

router = Router(auth=django_auth)

@router.get("/", response={200: list[UserSchema]})
def list_backlog(request):
    
