from django.utils.translation import gettext_lazy as _
from rest_framework import permissions


class IsUserStudent(permissions.BasePermission):
    """
    Check if authenticated user is an student.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'S':
            return True


class IsUserTeacher(permissions.BasePermission):
    """
    Check if authenticated user is a teacher.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'T':
            return True
