from rest_framework import permissions
from rest_framework.views import View, Request
from .models import Account
from courses.models import Course


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_superuser)
        
        
class IsStudentAssociated(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
                request.user.is_authenticated
                and request.user.is_superuser)


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Account) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and obj == request.user


class IsSuperuserOrParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True      
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            content = view.get_object()
            if request.user in content.course.students.all():
                return True
            return False
        