from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantRecordModelSerializer

User = get_user_model()


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Assignee : 상백

    access token과 refresh token를 발행해주는 시리얼라이저입니다.
    로그인 시, 유저에게 응답해주기 위해 설정합니다.
    """

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


class SignUpSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    User 모델을 위한 회원가입 시리얼라이저입니다.
    회원가입 시, email에 대한 유효성 검사를 진행합니다.
    """

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User(email=email, password=password)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("email", "password")


class SignInSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    User 모델 로그인 시리얼라이저입니다.
    로그인 시, email과 password를 확인합니다.
    """

    class Meta:
        model = User
        fields = ("email", "password")


class RestaurantTrashSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    유저의 가계부 삭제 목록을 응답하기 위한 시리얼라이저입니다.
    가계부의 가계부 고유번호와 이름, 삭제여부를 보여줍니다.
    """

    가계부_고유번호 = serializers.IntegerField(source="id", required=False, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("가계부_고유번호", "name", "is_deleted")


class RestaurantRecordTrashSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    유저의 특정 가계부에 속해있는 레코드 삭제 목록을 응답하기 위한 시리얼라이저입니다.
    레코드와 관련된 정보 및 삭제여부를 보여줍니다.
    """

    restaurant_records = serializers.SerializerMethodField(required=False, read_only=True)

    def get_restaurant_records(self, obj):
        restaurant_records = obj.restaurant_record.order_by("-created_at").filter(is_deleted=True)
        restaurant_records_serializer = RestaurantRecordModelSerializer(restaurant_records, many=True)
        return restaurant_records_serializer.data

    class Meta:
        model = Restaurant
        fields = ("name", "user", "restaurant_records")
