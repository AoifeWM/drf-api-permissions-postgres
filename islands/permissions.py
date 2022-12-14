from rest_framework import permissions


class OwnershipRequired(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.contributor is None:
            return True

        return obj.contributor == request.user
