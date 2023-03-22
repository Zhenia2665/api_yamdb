from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS
                    or request.user and request.user.is_authenticated)

    # def has_object_permission(self, request, view, obj):
    #     if request.method in SAFE_METHODS and\
    #         request.user == obj.author and\
    #             request.user.is_moderator or request.user.is_admin:
    #         return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.user == obj.author:
            return True

        if request.user.is_moderator or request.user.is_admin:
            return True

        return False


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (request.user and request.user.is_authenticated
                and request.user.is_admin)


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated
                and request.user.is_admin)
