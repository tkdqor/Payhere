from django.urls import path

from .views import RestaurantAPIView, RestaurantDetailAPIView, RestaurantRecordAPIView, RestaurantRecordDetailAPIView

app_name = "restaurant"

urlpatterns = [
    path("api/v1/restaurants", RestaurantAPIView.as_view()),
    path("api/v1/restaurants/<restaurant_id>", RestaurantDetailAPIView.as_view()),
    path("api/v1/restaurants/<restaurant_id>/records", RestaurantRecordAPIView.as_view()),
    path("api/v1/restaurants/<restaurant_id>/records/<record_id>", RestaurantRecordDetailAPIView.as_view()),
]
