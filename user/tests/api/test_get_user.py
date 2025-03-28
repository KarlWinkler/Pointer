import pytest

from user.tests.factories.user_factory import UserFactory


@pytest.mark.django_db
def test_returns_user_when_exist(client, user):
    response = client.get(f"/api/user/{user.id}")

    assert response.status_code == 200
    assert response.json().get('first_name') == user.first_name


@pytest.mark.django_db
def test_returns_404_when_does_not_exist(client, user):
    response = client.get(f"/api/user/{user.id + 1}")

    assert response.status_code == 404


@pytest.mark.django_db
def test_returns_401_when_unauthorized(client):
    response = client.get(f"/api/user/1")

    assert response.status_code == 401
