from django.urls import path
from . import views



Urlpatterns = [
    path("register/", views.register_student, name = "register"),
]