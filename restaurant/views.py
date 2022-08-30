from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwner
from restaurant.models import Restaurant, RestaurantRecord

from .serializers import RestaurantModelSerializer, RestaurantRecordListModelSerializer, RestaurantRecordModelSerializer


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


# url : GET,PUT api/v1/restaurants/<restaurant_id>
class RestaurantDetailAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능
    Http method = GET, PUT
    GET : 특정 가계부 조회
    PUT : 특정 가계부 수정
    """

    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 상백

        restaurant_id로 들어온 id에 해당하는 객체가 있는지 검토하는 메서드입니다.
        존재하지 않아 DoesNotExist 에러가 발생할 경우 None을 리턴합니다.
        """

        try:
            object = Restaurant.objects.get(id=obj_id, is_deleted=False)
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

    def put(self, request, restaurant_id):
        """
        Assignee : 상백

        특정 가계부를 수정하기 위한 메서드입니다. 가계부 목록 조회에서 볼 수 있는 가계부 고유번호가 필요합니다.
        restaurant_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        is_deleted 정보를 수정하려는 경우에도 에러 메시지를 응답합니다.
        ex) {"name": "이디야커피 발산점","balance": "500000"}
        """

        if request.data.get("is_deleted", None) is not None:
            return Response({"error": "변경할 수 없는 정보입니다. name와 balance만 수정이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        restaurant = self.get_object_and_check_permission(restaurant_id)
        if not restaurant:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = RestaurantModelSerializer(restaurant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "해당 가계부 정보가 수정되었습니다."}, status=status.HTTP_200_OK)


# url : GET, POST api/v1/restaurants/<restaurant_id>/records
class RestaurantRecordAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능
    Http method = GET, POST
    GET : 특정 가계부에 속하는 레코드 조회
    POST : 특정 가계부에 속하는 레코드 생성
    """

    permission_classes = [IsOwner]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 상백

        restaurant_id로 들어온 id에 해당하는 객체가 있는지 검토하는 메서드입니다.
        존재하지 않아 DoesNotExist 에러가 발생할 경우 None을 리턴합니다.
        """

        try:
            object = Restaurant.objects.get(id=obj_id, is_deleted=False)
        except Restaurant.DoesNotExist:
            return None

        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, restaurant_id):
        """
        Assignee : 상백

        특정 가계부에 속하는 레코드(금액, 메모)들을 조회할 수 있게 해주는 메서드입니다.
        RestaurantRecordListModelSerializer를 이용해서 특정 가계부의 속한 레코드들을 보여주고
        초기 잔액과 현재 잔액을 파악할 수 있습니다.
        """

        restaurant = self.get_object_and_check_permission(restaurant_id)
        if not restaurant:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(RestaurantRecordListModelSerializer(restaurant).data, status=status.HTTP_200_OK)

    def post(self, request, restaurant_id):
        """
        Assignee : 상백

        클라이언트가 POST 요청을 하고 가계부 고유번호를 입력하면, 해당 가계부에 속한 금액과 메모 레코드를 생성하는 메서드입니다.
        context 딕셔너리로 Restaurant 객체를 보내서 클라이언트가 가계부 고유번호 id를 입력하지 않게 설정했습니다.
        ex) {"amount": "20000","memo": "카드매출"}
        """

        restaurant = self.get_object_and_check_permission(restaurant_id)
        if not restaurant:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            context = {"restaurant": restaurant}
            serializer = RestaurantRecordModelSerializer(data=request.data, context=context)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# url : GET,PUT,PATCH api/v1/restaurants/<restaurant_id>/records/<record_id>
class RestaurantRecordDetailAPIView(APIView):
    """
    Assignee : 상백

    permission = 작성자 본인만 가능 - 각 메소드 내부에서 예외처리로 진행
    Http method = GET, PUT, PATCH
    GET : 특정 가계부에 속하는 특정 레코드 조회
    PUT : 특정 가계부에 속하는 특정 레코드 수정
    PATCH : 특정 가계부에 속하는 특정 레코드 삭제
    """

    permission_classes = [IsOwner]

    def get(self, request, restaurant_id, record_id):
        """
        Assignee : 상백

        특정 가계부에 속하는 특정 레코드를 조회하기 위한 메서드입니다.
        가계부 목록 조회에서 볼 수 있는 가계부 고유번호와 특정 가계부에 속하는 레코드 조회에서 볼 수 있는 레코드 고유번호가 필요합니다.
        restaurant_id로 존재하는 객체 또는 record_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        """

        try:
            restaurant = Restaurant.objects.get(user=request.user, id=restaurant_id, is_deleted=False)
            restaurant_record = RestaurantRecord.objects.get(restaurant=restaurant, id=record_id, is_deleted=False)
            return Response(RestaurantRecordModelSerializer(restaurant_record).data, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        except RestaurantRecord.DoesNotExist:
            return Response({"error": "해당 record_id로 존재하는 레코드가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, restaurant_id, record_id):
        """
        Assignee : 상백

        특정 가계부에 속하는 특정 레코드를 수정하기 위한 메서드입니다.
        가계부 목록 조회에서 볼 수 있는 가계부 고유번호와 특정 가계부에 속하는 레코드 조회에서 볼 수 있는 레코드 고유번호가 필요합니다.
        restaurant_id로 존재하는 객체 또는 record_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        또한, is_deleted나 date 정보를 수정하려고 해도 에러 메시지를 응답합니다.
        ex) {"amount": "20000","memo": "카드매출"}
        """

        if request.data.get("is_deleted", None) or request.data.get("date", None) is not None:
            return Response({"error": "변경할 수 없는 정보입니다. amount와 memo만 수정이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            restaurant = Restaurant.objects.get(user=request.user, id=restaurant_id, is_deleted=False)
            restaurant_record = RestaurantRecord.objects.get(restaurant=restaurant, id=record_id, is_deleted=False)
            serializer = RestaurantRecordModelSerializer(restaurant_record, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "해당 레코드 정보가 수정되었습니다."}, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        except RestaurantRecord.DoesNotExist:
            return Response({"error": "해당 record_id로 존재하는 레코드가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, restaurant_id, record_id):
        """
        Assignee : 상백

        특정 가계부에 속하는 특정 레코드를 삭제하기 위한 메서드입니다.
        가계부 목록 조회에서 볼 수 있는 가계부 고유번호와 특정 가계부에 속하는 레코드 조회에서 볼 수 있는 레코드 고유번호가 필요합니다.
        restaurant_id로 존재하는 객체 또는 record_id로 존재하는 객체가 없다면 에러 메시지를 응답합니다.
        is_deleted 필드를 true로 설정 후 JSON 형태로 요청하면 삭제 처리가 되고, false로 설정 후 JSON 형태로 요청하면 복구가 됩니다.
        ex) {"is_deleted": true} 또는 {"is_deleted": false}
        """

        if (
            request.data.get("amount", None)
            or request.data.get("memo", None)
            or request.data.get("date", None) is not None
        ):
            return Response({"error": "변경할 수 없는 정보입니다. is_deleted만 수정이 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            restaurant = Restaurant.objects.get(user=request.user, id=restaurant_id, is_deleted=False)
            restaurant_record = RestaurantRecord.objects.get(restaurant=restaurant, id=record_id)
            if request.data["is_deleted"] == True:
                restaurant_record.is_deleted = True
                restaurant_record.save()
                return Response({"message": "해당 레코드를 삭제했습니다!"}, status=status.HTTP_200_OK)
            elif request.data["is_deleted"] == False:
                restaurant_record.is_deleted = False
                restaurant_record.save()
                return Response({"message": "해당 레코드를 복구했습니다!"}, status=status.HTTP_200_OK)
        except Restaurant.DoesNotExist:
            return Response(
                {"error": "해당 restaurant_id로 존재하는 가계부가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND
            )
        except RestaurantRecord.DoesNotExist:
            return Response({"error": "해당 record_id로 존재하는 레코드가 없으니 다시 한 번 확인해주세요!"}, status=status.HTTP_404_NOT_FOUND)
