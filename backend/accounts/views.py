from typing import TYPE_CHECKING

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from accounts.serializers import UserSerializer

if TYPE_CHECKING:
    from typing import ClassVar

    from rest_framework.authentication import BaseAuthentication
    from rest_framework.permissions import BasePermission


class UserViewSet(ModelViewSet[CustomUser]):
    authentication_classes: ClassVar[list[BaseAuthentication]] = [SessionAuthentication]
    permission_classes: ClassVar[list[BasePermission]] = [AllowAny]

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
