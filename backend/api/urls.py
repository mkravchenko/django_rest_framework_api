from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("", views.home),
    path("auth/", obtain_auth_token),
    path("products/", include("products.urls")),
]
