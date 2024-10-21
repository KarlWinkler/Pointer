import pytest
import json

from user.models import User
from user.api import router
from user.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_signs_up_user_with_valid_credentials(client):
    data = {
        "email": "username@email.com",
        "first_name": "user",
        "last_name": "name",
        "password": "user_password",
    }

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 201
    assert response.json()["email"] == data["email"]
    assert response.json()["first_name"] == data["first_name"]
    assert response.json()["last_name"] == data["last_name"]


@pytest.mark.django_db
def test_does_not_sign_up_user_missing_email(client):
    data = {
        "first_name": "user",
        "last_name": "name",
        "password": "user_password",
    }

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 422


@pytest.mark.django_db
def test_does_not_sign_up_user_missing_password(client):
    data = {
        "email": "username@email.com",
        "first_name": "user",
        "last_name": "name",
    }

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 422


@pytest.mark.django_db
def test_does_not_sign_up_user_missing_first_name(client):
    data = {
        "email": "username@email.com",
        "last_name": "name",
        "password": "user_password",
    }

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 422


@pytest.mark.django_db
def test_does_not_sign_up_user_missing_last_name(client):
    data = {
        "email": "username@email.com",
        "first_name": "user",
        "password": "user_password",
    }

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 422


@pytest.mark.django_db
def test_does_not_sign_up_user_empty(client):
    data = {}

    response = client.post('/api/user/signup', json.dumps(data), content_type='application/json')

    assert response.status_code == 422
