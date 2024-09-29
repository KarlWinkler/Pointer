import pytest
import json 

from user.models import User
from user.api import router
from user.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_logs_in_user_with_correct_credentials(client):  
    data = {
        "password": "user_password",
        "username": "username",
    }

    user = UserFactory(username='username')
    user.set_password('user_password')
    user.save()

    response = client.post('/api/user/login', json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json()["username"] == user.username
    assert response.json()["first_name"] == user.first_name
    assert response.json()["last_name"] == user.last_name


@pytest.mark.django_db
def test_does_not_log_in_user_with_bad_credentials(client):
    data = {
        "password": "user_bad",
        "username": "userbad",
    }

    user = UserFactory(username='username')
    user.set_password('user_password')
    user.save()

    response = client.post('/api/user/login', json.dumps(data), content_type='application/json')

    assert response.status_code == 401
