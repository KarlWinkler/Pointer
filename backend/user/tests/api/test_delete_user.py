import pytest

from user.tests.factories.user_factory import UserFactory
from user.models import User


@pytest.mark.django_db
def test_user_deleted_if_exists(client, user):
    response = client.delete(f"/api/user/{user.id}")

    assert response.status_code == 200
    assert not User.objects.filter(id=user.id).exists()


@pytest.mark.django_db
def test_returns_404_when_does_not_exist(client, user):
    response = client.delete(f"/api/user/{user.id + 1}")

    assert response.status_code == 404


@pytest.mark.django_db
def test_user_not_deleted_when_unauthorized(client):
    user = UserFactory()
    response = client.delete(f"/api/user/{user.id}")

    assert response.status_code == 401
    assert User.objects.filter(id=user.id).exists()
