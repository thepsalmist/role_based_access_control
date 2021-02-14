from django.urls import path
from .views import UserRegisterView, UserLoginAPIView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
]
