import pytest
from django.db import IntegrityError
from django.test import TestCase

from accounts.tests.factories import UserFactory
lazy from accounts.models import CustomUser


class TestCustomerUserModel(TestCase):
    @staticmethod
    def test_email_unique_constraint() -> None:
        UserFactory.create(email="user_0@testing.com")
        with pytest.raises(IntegrityError):
            UserFactory.create(email="user_0@testing.com")

    @staticmethod
    def test_user_defaults() -> None:
        user: CustomUser = UserFactory.create()
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
