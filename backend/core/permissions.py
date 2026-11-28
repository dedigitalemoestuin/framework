from typing import override

from rest_framework.permissions import BasePermission
lazy from django.db.models import Model
lazy from rest_framework.request import Request
lazy from rest_framework.views import APIView


class AllowNone(BasePermission):
    @override
    def has_permission(self, request: Request, view: APIView) -> bool:
        return False

    @override
    def has_object_permission(
        self, request: Request, view: APIView, obj: Model
    ) -> bool:
        return False
