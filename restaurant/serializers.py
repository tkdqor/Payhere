from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Restaurant


class RestaurantModelSerializer(ModelSerializer):
    """
    Assignee : 상백

    가계부_고유번호라는 필드로 특정 가계부의 번호를 응답해줍니다.
    create 메소드를 통해 로그인된 user로 Restaurant 모델 객체를 생성합니다.
    """

    가계부_고유번호 = serializers.IntegerField(source="id", required=False, read_only=True)

    def create(self, validated_data):
        user = self.context["user"]
        restaurant = Restaurant(user=user, **validated_data)
        restaurant.save()
        return restaurant

    class Meta:
        model = Restaurant
        fields = ("name", "가계부_고유번호", "user", "balance", "is_deleted", "created_at", "updated_at")
        read_only_fields = ["user", "is_deleted", "created_at", "updated_at"]
