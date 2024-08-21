from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """
        This permission will allow all access to only authors os the todo list
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user