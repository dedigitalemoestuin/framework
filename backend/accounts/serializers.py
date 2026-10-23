from typing import TYPE_CHECKING

from rest_framework import serializers

from accounts.models import CustomUser

if TYPE_CHECKING:
    from typing import ClassVar


class UserSerializer(serializers.ModelSerializer[CustomUser]):
    class Meta:
        model = CustomUser
        fields: ClassVar[list[str]] = ["id", "email"]
