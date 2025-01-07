from rest_framework import permissions

class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'владелец'

class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

