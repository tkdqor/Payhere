from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import RestaurantRecordTrashView, RestaurantTrashView, SignInView, SignUpView

app_name = "accounts"

urlpatterns = [
    path("v1/users/signup", SignUpView.as_view()),
    path("v1/users/signin", SignInView.as_view()),
    path("v1/token/refresh", TokenRefreshView.as_view()),
    path("v1/users/restaurants/trash", RestaurantTrashView.as_view()),
    path("v1/users/restaurants/<restaurant_id>/trash", RestaurantRecordTrashView.as_view()),
]
