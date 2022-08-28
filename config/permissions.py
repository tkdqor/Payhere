from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Assignee : 상백

    has_permission : 로그인 한 유저는 모두 접근 가능
    has_object_permission(오브젝트 접근 권한)
    - 작성자가 본인일 경우에만 접근 가능하도록 설정
    - 관리자는 모든 접근 가능
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return request.user.is_authenticated
        # return obj.user.id == request.user.id
        if request.user.is_authenticated:
            if request.user.is_admin:
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == request.user.id
            elif hasattr(obj, "user"):
                return obj.user.id == request.user.id
            elif hasattr(obj, "restaurant"):
                return obj.restaurant.user.id == request.user.id
            return False
        return False
