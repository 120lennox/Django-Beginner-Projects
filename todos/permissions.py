from rest_framework import permissions

class IsAuthor(permissions.BasePermission):
    """
        Allows Access to only authors of the todo list
    """
    def has_object_permission(self, request, view, obj):
        # checks if the user is the author 
        obj.author == request.user
    