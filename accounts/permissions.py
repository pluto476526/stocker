# accounts/permissions.py

from rest_framework.permissions import BasePermission

class IsSuperUserOnly(BasePermission):
    """
    Custom permission that only allows superusers to view, edit, or delete users.
    """
    def has_permission(self, request, view):
        """
        Check if user is a superuser
        """
        profile = request.user.profile
        return request.user.is_authenticated and profile.in_superusers

