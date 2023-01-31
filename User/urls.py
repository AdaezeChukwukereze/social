from django.urls import path
from .views import home_page, register




urlpatterns = [
    path("",home_page,name="home"),
    path("register/",register, name="register")
]