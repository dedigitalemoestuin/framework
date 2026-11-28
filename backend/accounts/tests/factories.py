from factory.declarations import Sequence
from factory.django import DjangoModelFactory, Password

from accounts.models import CustomUser


class UserFactory(DjangoModelFactory[CustomUser]):
    class Meta:
        model = CustomUser

    email = Sequence(lambda n: f"user_{n}@testing.com")
    password = Password("strongpassword")
