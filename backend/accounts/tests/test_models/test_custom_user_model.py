from typing import TYPE_CHECKING

import pytest
from django.db import IntegrityError
from django.test import TestCase

from accounts.tests.factories import UserFactory

if TYPE_CHECKING:
    from accounts.models import CustomUser


class TestCustomerUserModel(TestCase):
    def test_email_unique_constraint(self) -> None:
        UserFactory(email="user_0@testing.com")
        with pytest.raises(IntegrityError):
            UserFactory(email="user_0@testing.com")

    def test_user_defaults(self) -> None:
        user: CustomUser = UserFactory()
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
