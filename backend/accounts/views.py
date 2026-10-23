from typing import TYPE_CHECKING

from django.contrib.auth import views as auth_views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomUser
from accounts.serializers import UserSerializer

if TYPE_CHECKING:
    from collections.abc import Sequence

    from rest_framework.authentication import BaseAuthentication
    from rest_framework.permissions import BasePermission

# DRF APIs


class UserViewSet(ModelViewSet[CustomUser]):
    authentication_classes: Sequence[type[BaseAuthentication]] = [SessionAuthentication]
    permission_classes: Sequence[type[BasePermission]] = [AllowAny]

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


# Django authentication views


class LoginView(auth_views.LoginView):
    pass


class LogoutView(auth_views.LogoutView):
    pass


class PasswordChangeView(auth_views.PasswordChangeView):
    pass


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    pass


class PasswordResetView(auth_views.PasswordResetView):
    pass


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    pass


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    pass


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    pass
