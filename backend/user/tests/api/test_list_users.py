import pytest


@pytest.mark.django_db
def test_returns_all_users_when_authenticated(client, user):  
    response = client.get('/api/user/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_returns_401_when_unauthourized(client):  
    response = client.get('/api/user/')

    assert response.status_code == 401
