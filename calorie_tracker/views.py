from django.shortcuts import render, redirect
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
    
    if request.method == "POST":
        title = request.POST.get("title")
        calorie_amount = request.POST.get("calorie_amount")
        if title and calorie_amount:
            FoodItem.objects.create(title=title, calorie_amount=calorie_amount)
            return redirect("home")
    food_items = FoodItem.objects.all()
    

    total_calories = 0
    for cal in food_items:
        total_calories += cal.calorie_amount
    context = {"message":"Calorie Tracker", "food_items": food_items, "total_calories": total_calories}
    return render(request, "calorie_tracker/contact.html", context)

def delete_food(request, id):
    if request.method == "POST":
        item = FoodItem.objects.get(id=id)
        item.delete()
    return redirect("home")
def reset_calories(request):
    if request.method == "POST":
        FoodItem.objects.all().delete()
    return redirect("home")
