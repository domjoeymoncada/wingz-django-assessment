from rest_framework import permissions
from apps.user.models import UserRole


class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == UserRole.ADMIN
        )