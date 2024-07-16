from django.urls import path
from .views import ImUserLogin

urlpatterns = [
    path("login/", ImUserLogin.as_view(), name="login")
]
