from django.contrib import admin
from .models import FoodItem, Author

# Register your models here.
admin.site.register(Author)
admin.site.register(FoodItem)
