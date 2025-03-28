import pytest
from user.tests.factories.user_factory import UserFactory

@pytest.fixture
def user(client):
    user = UserFactory(email='default@email.com')
    user.set_password('user_password')
    user.save()

    request = client.login(email='default@email.com', password='user_password')

    return user