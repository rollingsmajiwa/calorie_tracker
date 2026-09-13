from django.shortcuts import render
from .models import FoodItem

# Create your views here.
def calorie_list(request):
    context = {"name" : "Collo", "age": 28}
    return render(request, "index.html", context)