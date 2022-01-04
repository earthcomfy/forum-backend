from django.utils.translation import gettext_lazy as _

from rest_framework import permissions


class IsUserAuthor(permissions.BasePermission):
    """
    Check if authenticated user is an author of the question.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
