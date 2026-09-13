from django.shortcuts import render
from .models import FoodItem

# Create your views here.
def calorie_list(request):
    context = {"name" : "Collo", "age": 28}
    return render(request, "calorie_tracker/index.html", context)
def aboutproject(request):
    context = {"message": "Wecome to my About section"}
    return render(request, "calorie_tracker/about.html", context)
def servicesproject(request):
    context = {"message": "Wecome to my services section"}
    return render(request, "calorie_tracker/services.html", context)
def contactproject(request):
    context = {"message": "Wecome to my contact section"}
    return render(request, "calorie_tracker/contact.html", context)