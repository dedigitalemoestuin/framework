from typing import TYPE_CHECKING

from rest_framework import serializers

from accounts.models import CustomUser

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import ClassVar


class UserSerializer(serializers.ModelSerializer[CustomUser]):
    class Meta:
        model = CustomUser
        fields: ClassVar[Sequence[str]] = ["id", "email"]
