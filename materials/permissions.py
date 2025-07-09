from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderators').exists():
            return True


class IsModeratorForbidden(BasePermission):

    def has_permission(self, request, view):
        return not request.user.groups.filter(name='moderators').exists()


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().owner
