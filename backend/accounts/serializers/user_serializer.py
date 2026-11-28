lazy from collections.abc import Sequence
lazy from typing import ClassVar

from rest_framework import serializers

from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer[CustomUser]):
    class Meta:
        model = CustomUser
        fields: ClassVar[Sequence[str]] = ["id", "email"]
