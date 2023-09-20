from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "You need to be Moderator for this action"

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return False


class IsOwner(BasePermission):
    message = "You need to be creator of the object for this action"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.creator:
            # if request.user == view.get_object().creator:
            return True
        return False


class IsAdministrator(BasePermission):
    message = "You need to be Admin for this action"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
