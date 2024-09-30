import factory
from factory import Faker

class UserFactory(factory.django.DjangoModelFactory):
    username = Faker('name')
    first_name = Faker('last_name')
    last_name = Faker('last_name')
    email = Faker('email')
    preferences = Faker('json')

    class Meta:
        model = "user.User"
