import pytest
import json


@pytest.mark.django_db
def test_updates_user_with_valid_data(client, user):
    data = {
        "email": "new@email.com",
        "first_name": "user",
        "last_name": "name",
    }
    response = client.put(f"/api/user/{user.id}", json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json()["email"] == data["email"]


@pytest.mark.django_db
def test_updates_user_with_partial_data(client, user):
    old_first_name = user.first_name
    data = {"email": "new@email.com"}

    response = client.put(f"/api/user/{user.id}", json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json()["email"] == data["email"]
    assert response.json()["first_name"] == old_first_name


@pytest.mark.django_db
def test_does_not_create_user_when_unauthenticated(client):
    data = {
        "email": "username@email.com",
        "first_name": "user",
        "last_name": "name",
    }
    response = client.put("/api/user/1", json.dumps(data), content_type='application/json')

    assert response.status_code == 401