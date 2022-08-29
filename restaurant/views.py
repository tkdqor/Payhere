from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from restaurant.models import Restaurant

from .serializers import RestaurantModelSerializer


# url : GET, POST api/v1/restaurants
class RestaurantAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능
    Http method = GET, POST
    GET : 가계부 목록 조회
    POST : 가계부 생성
    """

    permission_classes = [IsOwner]

    def get(self, request):
        """
        Assignee : 상백

        가계부 목록을 조회할 수 있게 가계부 정보들을 response 하는 메서드입니다.
        로그인된 유저가 생성한 가계부 목록에서 삭제 되지 않은 목록만 보여줍니다.
        """

        restaurants = Restaurant.objects.filter(user=request.user, is_deleted=False).order_by("-created_at")
        serializer = RestaurantModelSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Assignee : 상백

        클라이언트의 요청 및 JSON 형태 데이터 입력 시, 가계부 데이터를 생성하는 메서드입니다.
        context 딕셔너리로 로그인된 유저 객체를 보내주어 클라이언트가 유저 id를 입력하지 않게 설정했습니다.
        ex) {"name": "이디야커피 발산점","balance": "500000"}
        """

        context = {"user": request.user}
        serializer = RestaurantModelSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
