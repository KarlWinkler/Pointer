import pytest
import json 

from user.models import User
from user.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_logs_in_user_with_correct_credentials(client):  
    data = {
        "email": "username@email.com",
        "password": "user_password",
    }

    user = UserFactory(email='username@email.com')
    user.set_password('user_password')
    user.save()

    response = client.post('/api/auth/login', json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json()["email"] == user.email
    assert response.json()["first_name"] == user.first_name
    assert response.json()["last_name"] == user.last_name


@pytest.mark.django_db
def test_does_not_log_in_user_with_bad_credentials(client):
    data = {
        "password": "user_bad",
        "email": "username@email.com",
    }

    user = UserFactory(email='username@email.com')
    user.set_password('user_password')
    user.save()

    response = client.post('/api/auth/login', json.dumps(data), content_type='application/json')

    assert response.status_code == 401
