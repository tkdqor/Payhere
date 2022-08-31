from rest_framework.test import APIClient, APITestCase

from accounts.models import User
from restaurant.models import Restaurant, RestaurantRecord


class RestaurantDetailAPIViewTestCase(APITestCase):
    """
    Assignee : 상백

    특정 가계부 조회 확인 테스트입니다.
    setUp 메서드로 유저와 Restaurant 객체를 생성합니다.
    해당 API로 GET 요청을 했을 때, 가계부 조회가 되어 status code 200을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/restaurants/1"

    def setUp(self):
        """유저 및 Restaurant 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="123456")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.restaurant = Restaurant.objects.create(user_id=self.user.id, name="이디야커피 강남점", balance=500000)

    def test_restaurant_detail(self):
        """Restaurant 객체 조회 테스트"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 200)


class RestaurantRecordDetailAPIViewTestCase(APITestCase):
    """
    Assignee : 상백

    특정 가계부에 속한 특정 레코드 조회 확인 테스트입니다.
    setUp 메서드로 유저와 Restaurant 그리고 RestaurantRecord 객체를 생성합니다.
    해당 API로 GET 요청을 했을 때, 특정 가계부에 속한 단일 레코드가 조회되어 status code 200을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/restaurants/1/records/1"

    def setUp(self):
        """유저 및 Restaurant 그리고 RestaurantRecord 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="123456")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.restaurant = Restaurant.objects.create(user_id=self.user.id, name="이디야커피 강남점", balance=500000)
        self.restaurantrecord = RestaurantRecord.objects.create(
            restaurant_id=self.restaurant.id, amount=50000, memo="카드매출"
        )

    def test_restaurantrecord_detail(self):
        """RestaurantRecord 객체 조회 테스트"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 200)


class RestaurantRecordAPIViewTestCase(APITestCase):
    """
    Assignee : 상백

    특정 가계부에 속한 레코드 조회 확인 테스트입니다.
    setUp 메서드로 유저와 Restaurant 그리고 RestaurantRecord 객체를 생성합니다.
    해당 API로 GET 요청을 했을 때, 특정 가계부에 속한 레코드가 조회되어 status code 200을 응답하는 것을 확인합니다.
    """

    url = "/api/v1/restaurants/1/records"

    def setUp(self):
        """유저 및 Restaurant 그리고 RestaurantRecord 객체 생성 설정"""
        self.user = User.objects.create(email="aaa@naver.com", password="123456")
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.restaurant = Restaurant.objects.create(user_id=self.user.id, name="이디야커피 강남점", balance=500000)
        self.restaurantrecord = RestaurantRecord.objects.create(
            restaurant_id=self.restaurant.id, amount=50000, memo="카드매출"
        )

    def test_restaurantrecord(self):
        """Restaurant에 속한 RestaurantRecord 객체 조회 테스트"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, 200)
