from rest_framework.permissions import BasePermission

class IsVerifiedUser(BasePermission):
    """
    Allows access only to users with is_verified=True.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and getattr(request.user, 'is_verified', False)
