lazy from collections.abc import Sequence

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
lazy from rest_framework.authentication import BaseAuthentication
lazy from rest_framework.permissions import BasePermission

from accounts.models import CustomUser
from accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet[CustomUser]):
    authentication_classes: Sequence[type[BaseAuthentication]] = [SessionAuthentication]
    permission_classes: Sequence[type[BasePermission]] = [AllowAny]

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
