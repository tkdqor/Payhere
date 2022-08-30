from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import (
    RestaurantTrashSerializer,
    SignInSerializer,
    SignUpSerializer,
    UserTokenObtainPairSerializer,
)
from config.permissions import IsOwner


# url : POST api/v1/users/signup
class SignUpView(APIView):
    """
    Assignee : 상백

    회원가입을 진행하는 APIView입니다.
    권한은 누구나 접근할 수 있게 설정하고 회원가입 성공 시, 201 code를 응답합니다.
    """

    permission_classes = [AllowAny]
    serializer = SignUpSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = Response(
                {
                    "message": "회원가입에 성공했습니다.",
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# url : POST api/v1/users/signin
class SignInView(APIView):
    """
    Assignee : 상백

    로그인을 진행하는 APIView입니다.
    로그인 성공 시, 클라이언트에게 access token과 refresh token을 리턴합니다.
    로그인에 실패할 경우, 404 code를 응답합니다.
    """

    permission_classes = [AllowAny]
    serializer = SignInSerializer

    def post(self, request):
        user = authenticate(request, email=request.data.get("email"), password=request.data.get("password"))
        if not user:
            return Response({"error": "이메일 또는 비밀번호를 잘못 입력했습니다."}, status=status.HTTP_404_NOT_FOUND)

        login(request, user)

        token = UserTokenObtainPairSerializer.get_token(user)

        res = Response(
            {
                "message": f"{user.email}님, 로그인이 완료되었습니다!",
                "token": {
                    "access": str(token.access_token),
                    "refresh": str(token),
                },
            },
            status=status.HTTP_200_OK,
        )
        return res


# url : GET api/v1/restaurants/trash
class RestaurantTrashView(APIView):
    """
    Assignee : 상백

    로그인된 유저의 가계부 삭제 목록을 응답해주는 APIView입니다.
    """

    permission_classes = [IsOwner]

    def get(self, request):
        """
        Assignee : 상백

        삭제된 가계부 목록을 response하는 메서드입니다.
        가계부 목록에서 로그인된 유저가 삭제처리를 진행하여 is_deleted가 True인 가계부 목록만 보여줍니다.
        """

        restaurants = request.user.user_restaurant.filter(is_deleted=True)
        serializer = RestaurantTrashSerializer(restaurants, many=True)
        if restaurants:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "해당 유저가 삭제한 가계부가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
