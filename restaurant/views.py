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
        if restaurants:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "해당 유저가 생성한 가계부가 없습니다. 가계부를 생성해주세요!"}, status=status.HTTP_404_NOT_FOUND)

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


# url : GET api/v1/restaurants/<restaurant_id>
class RestaurantDetailAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능
    Http method = GET
    GET : 특정 가계부 조회
    """

    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 상백

        restaurant_id로 들어온 id에 해당하는 객체가 있는지 검토하는 메서드입니다.
        존재하지 않아 DoesNotExist 에러가 발생할 경우 None을 리턴합니다.
        """
        try:
            object = Restaurant.objects.get(id=obj_id)
        except Restaurant.DoesNotExist:
            return None

        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, restaurant_id):
        """
        Assignee : 상백

        특정 가계부 조회를 하기 위한 메서드입니다. 가계부 목록 조회에서 볼 수 있는 가계부 고유번호가 필요합니다.
        restaurant_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        """

        restaurant = self.get_object_and_check_permission(restaurant_id)
        if not restaurant:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(RestaurantModelSerializer(restaurant).data, status=status.HTTP_200_OK)
