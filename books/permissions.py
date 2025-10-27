from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS (anyone can read)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only allow if the owner is the current user
        return obj.owner == request.user
