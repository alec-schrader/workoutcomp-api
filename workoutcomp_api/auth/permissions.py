from rest_framework.permissions import BasePermission, SAFE_METHODS

class HasPermission(BasePermission):
    permission = None

    """
    User is allowed access if has the expected permission
    """
    def has_permission(self, request, view):
        return request.auth and self.permission in request.auth.get('permissions', [])

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.owner == request.user



class HasAdminPermission(HasPermission):
    permission = "read:admin-messages"