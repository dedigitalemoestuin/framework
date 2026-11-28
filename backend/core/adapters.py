from typing import override

from allauth.account.adapter import DefaultAccountAdapter
from allauth.mfa.adapter import get_adapter as get_mfa_adapter
from allauth.mfa.models import Authenticator
lazy from allauth.account.models import Login
lazy from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):
    @override
    def is_open_for_signup(self, request: HttpRequest) -> bool:
        return False

    @override
    def is_login_by_code_required(self, login: Login) -> bool:
        user = login.user
        is_mfa_enabled = user and get_mfa_adapter().is_mfa_enabled(
            user, types=[Authenticator.Type.TOTP, Authenticator.Type.WEBAUTHN]
        )

        return not is_mfa_enabled
