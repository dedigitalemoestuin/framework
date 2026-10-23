from typing import TYPE_CHECKING, override

from rest_framework.permissions import BasePermission

if TYPE_CHECKING:
    from django.db.models import Model
    from rest_framework.request import Request
    from rest_framework.views import APIView


class AllowNone(BasePermission):
    @override
    def has_permission(self, request: Request, view: APIView) -> bool:
        return False

    @override
    def has_object_permission(
        self, request: Request, view: APIView, obj: Model
    ) -> bool:
        return False
