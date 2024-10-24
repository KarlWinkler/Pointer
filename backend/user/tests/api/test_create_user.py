import pytest
import json


@pytest.mark.django_db
def test_create_user_with_valid_data(client, user):
    data = {
        "email": "username@email.com",
        "first_name": "user",
        "last_name": "name",
        "password": "user_password",
    }
    response = client.post("/api/user/", json.dumps(data), content_type='application/json')

    assert response.status_code == 200
