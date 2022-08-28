from django.urls import path

from .views import RestaurantAPIView

app_name = "restaurant"

urlpatterns = [
    path("api/v1/restaurants", RestaurantAPIView.as_view()),
]
