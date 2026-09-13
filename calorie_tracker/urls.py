from django.urls import path
from . import views

urlpatterns = [
    path("", views.calorie_list, name="home"),
    path("about/ ", views.aboutproject, name="about"),
    path("services/", views.servicesproject, name="services"),
    path("/contact", views.contactproject, name="contact")
]