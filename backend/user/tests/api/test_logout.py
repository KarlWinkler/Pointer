import pytest
import json

from user.models import User
from user.api import router
from user.tests.factories.user_factory import UserFactory

@pytest.mark.django_db
def test_logs_out_user(client):

    user = UserFactory(username='username')
    user.set_password('user_password')
    user.save()

    client.login(username='username', password='user_password')

    assert user.is_authenticated

    response = client.post('/api/user/logout')

    assert response.status_code == 200
