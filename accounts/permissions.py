# accounts/permissions.py

from rest_framework.permissions import BasePermission

class IsSuperUserOrReadOnly(BasePermission):
    """
    Custom permission that only allows superusers to edit or delete users.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to superusers
        return request.user.is_authenticated and request.user.is_superuser

