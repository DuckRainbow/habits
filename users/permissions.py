from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка на владельца привычки"""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
