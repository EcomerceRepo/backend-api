from rest_framework import permissions
from .utils import getUserByToken


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        user = getUserByToken(request)
        if user == None:
            return False
        if user.role == 2:
            return True
        return False

class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        user = getUserByToken(request)
        if user == None:
            return False
        if user.role == 1:
            return True
        return False