from rest_framework import permissions

class isAuthenticatedAndCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if request.method == 'GET':
                return True
            return False
        return super().has_permission(request, view)

class IsStaffIsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        # if user is authenticated or not and methods doesn't include put or delete. Grant read permissions
        if request.user.is_authenticated or not request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True                    
            
        # if the user is a super user grant all permission, he can perform any operation on other authors post
        if request.user.is_staff:
            return True
        
        # if author of the post is logged in user grant write permission as well as safe methods permission
        return obj.author == request.user