from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import Router

from .models import User
from .schemas.error_schema import Error
from .schemas.user_schema import UserSchema, UserCreateSchema

from ninja.security import django_auth

router = Router(auth=django_auth)

@router.get("/", response={200: list[UserSchema]})
def list_users(request):
    return User.objects.all()


@router.get("/{id}", response={404: Error, 200: UserSchema})
def get_user(request, id: int):
    return get_object_or_404(User, id=id)


@router.post("/", response={400: Error, 200: UserSchema})
def create_user(request, userCreateSchema: UserCreateSchema):
    try:
        user = User.objects.create(
            email=userCreateSchema.email,
            first_name=userCreateSchema.first_name,
            last_name=userCreateSchema.last_name,
        )
        user.set_password(userCreateSchema.password)
        user.save()

        return user
    except:
        return 400, {"message": "Failed to create user"}
