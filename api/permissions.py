from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    message = "You are not the owner or this article. Go away! You're naughty..."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.owner == request.user:
            return True
        return False