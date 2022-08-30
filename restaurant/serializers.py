from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Restaurant, RestaurantRecord


class RestaurantModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    가계부_고유번호라는 필드로 특정 가계부의 번호를 응답해줍니다.
    create 메소드를 통해 로그인된 user로 Restaurant 모델 객체를 생성합니다.
    현재 잔액을 응답하기 위해, 초기 잔액에다가 for문으로 RestaurantRecord 모델 객체들의 금액을 더해준 값을 SerializerMethodField로 설정합니다.
    """

    가계부_고유번호 = serializers.IntegerField(source="id", required=False, read_only=True)
    initial_balance = serializers.IntegerField(source="balance", required=False, read_only=True)
    current_balance = serializers.SerializerMethodField(required=False, read_only=True)

    def get_current_balance(self, obj):
        restaurant_records = obj.restaurant_record.order_by("-created_at").filter(is_deleted=False)
        current_balance = obj.balance
        for record in restaurant_records:
            current_balance += record.amount
        return current_balance

    def create(self, validated_data):
        user = self.context["user"]
        restaurant = Restaurant(user=user, **validated_data)
        restaurant.save()
        return restaurant

    class Meta:
        model = Restaurant
        fields = (
            "name",
            "가계부_고유번호",
            "user",
            "initial_balance",
            "current_balance",
            "is_deleted",
            "created_at",
            "updated_at",
        )
        read_only_fields = ["user", "is_deleted", "created_at", "updated_at"]


class RestaurantRecordModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    가계부 레코드마다 잔액을 응답하기 위해, RestaurantRecord 객체에서 참조 및 역참조를 진행해 현재 레코드까지의 RestaurantRecord 객체들을 가져오고
    가계부 초기 잔액부터 현재 객체와 비교해서 생성일이 같거나 더 큰 경우를 만족하는 객체들만 더해준 값을 SerializerMethodField로 설정합니다.
    create 메소드를 통해 특정 Restaurant 모델 객체와 1:N관계가 형성된 RestaurantRecord 모델 객체를 생성합니다.
    """

    가계부_고유번호 = serializers.IntegerField(source="restaurant_id", required=False, read_only=True)
    레코드_고유번호 = serializers.IntegerField(source="id", required=False, read_only=True)
    balance = serializers.SerializerMethodField(required=False, read_only=True)

    def get_balance(self, obj):
        balance = obj.restaurant.balance
        for record in obj.restaurant.restaurant_record.order_by("-created_at").filter(is_deleted=False):
            if obj.created_at >= record.created_at:
                balance += record.amount
        return balance

    def create(self, validated_data):
        restaurant = self.context["restaurant"]
        restaurant_record = RestaurantRecord(restaurant=restaurant, **validated_data)
        restaurant_record.save()
        return restaurant_record

    class Meta:
        model = RestaurantRecord
        fields = ("가계부_고유번호", "레코드_고유번호", "date", "amount", "balance", "memo", "is_deleted", "created_at", "updated_at")
        read_only_fields = ["가계부_고유번호", "레코드_고유번호", "date", "balance", "is_deleted", "created_at", "updated_at"]


class RestaurantRecordListModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    View에서 Restaurant 모델 객체가 전달될 때, 역참조를 진행해 해당 객체와 1:N 관계에 있는 RestaurantRecord 모델 객체들을 가져옵니다.
    현재 잔액을 응답하기 위해, 초기 잔액에다가 for문으로 RestaurantRecord 모델 객체들의 금액을 더해준 값을 SerializerMethodField로 설정합니다.
    """

    restaurant_records = serializers.SerializerMethodField(required=False, read_only=True)
    initial_balance = serializers.IntegerField(source="balance", required=False, read_only=True)
    current_balance = serializers.SerializerMethodField(required=False, read_only=True)

    def get_restaurant_records(self, obj):
        restaurant_records = obj.restaurant_record.order_by("-created_at").filter(is_deleted=False)
        restaurant_records_serializer = RestaurantRecordModelSerializer(restaurant_records, many=True)
        return restaurant_records_serializer.data

    def get_current_balance(self, obj):
        restaurant_records = obj.restaurant_record.order_by("-created_at").filter(is_deleted=False)
        current_balance = obj.balance
        for record in restaurant_records:
            current_balance += record.amount
        return current_balance

    class Meta:
        model = Restaurant
        fields = ("name", "user", "initial_balance", "current_balance", "restaurant_records")
        read_only_fields = ["initial_balance", "current_balance", "restaurant_records"]
