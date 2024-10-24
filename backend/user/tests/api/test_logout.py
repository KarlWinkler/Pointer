import pytest
import json

from user.models import User
from user.api import router

@pytest.mark.django_db
def test_logs_out_user(client, user):
    assert user.is_authenticated

    response = client.post('/api/user/logout')

    assert response.status_code == 200
