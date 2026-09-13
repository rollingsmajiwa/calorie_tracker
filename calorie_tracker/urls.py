from django.urls import path
from . import views

urlpatterns = [
    path("", views.calorie_list, name="calorie_list")
]