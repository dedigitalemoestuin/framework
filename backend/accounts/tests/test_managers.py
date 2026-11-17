import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagersTests(TestCase):
    def test_create_user(self) -> None:
        User = get_user_model()  # noqa: N806
        user = User.objects.create_user(email="normal@user.com", password="foo")

        assert user.email == "normal@user.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser

        with pytest.raises(TypeError, match="missing 2 required positional arguments"):
            User.objects.create_user()  # type: ignore[call-arg]
        with pytest.raises(TypeError, match="missing 1 required positional argument"):
            User.objects.create_user(email="normal@user.com")  # type: ignore[call-arg]
        with pytest.raises(ValueError, match="The Email must be set"):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self) -> None:
        User = get_user_model()  # noqa: N806
        admin_user = User.objects.create_superuser(
            email="super@user.com",
            password="foo",
        )

        assert admin_user.email == "super@user.com"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser

        with pytest.raises(ValueError, match="Superuser must have is_superuser=True"):
            User.objects.create_superuser(
                email="super@user.com",
                password="foo",
                is_superuser=False,
            )
