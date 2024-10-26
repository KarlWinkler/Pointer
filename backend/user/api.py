from django.shortcuts import get_object_or_404
from django.urls import path
from ninja import Router

from .models import User
from .schemas.error_schema import Error
from .schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema

from ninja.security import django_auth

router = Router(auth=django_auth)

@router.get("/", response={200: list[UserSchema]})
def list_users(request):
    return User.objects.all()


@router.get("/{id}", response={200: UserSchema})
def get_user(request, id: int):
    return get_object_or_404(User, id=id)


@router.post("/", response={201: UserSchema})
def create_user(request, data: UserCreateSchema):
    user = User.objects.create(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
    )
    user.set_password(data.password)
    user.save()

    return 201, user


@router.put("/{id}", response={200: UserSchema})
def update_user(request, id: int, data: UserUpdateSchema):
    user = get_object_or_404(User, id=id)

    for attr, value in data.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()

    return 200, user
