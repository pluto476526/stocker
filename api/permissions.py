from rest_framework.permissions import BasePermission, SAFE_METHODS
from api.models import WareHouse


class IsManagerOrReadOnly(BasePermission):
    """
    Custom permission to only allow managers of a warehouse to update products.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed for authenticated users
        # SAFE METODS = GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # For write permissions, check the manager
        if request.method == 'POST':
            wh_id = request.data.get('warehouse')
            try:
                warehouse = WareHouse.objects.get(pk=wh_id)
            except WareHouse.DoesNotExist:
                return False
            return request.user.is_authenticated and warehouse.manager == request.user

        # Default for other methods
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and # User must be authenticated
            hasattr(obj.warehouse, 'manager') and # Check if warehouse has a manager
            obj.warehouse.manager == request.user # Check if the user is the warehouse manager
        )


class IsSuperUserOrReadOnly(BasePermission):
    """
    Custom write permissions for superusers and read only permissions for evryone else
    """
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        profile = request.user.profile
        return request.user.is_authenticated and profile.in_superusers
