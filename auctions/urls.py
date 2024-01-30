from django.urls import path

from . import views
from .views import create_listing

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path('create_listing/', create_listing, name='create_listing')
]
