from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class FoodItem(models.Model):
    title = models.CharField(max_length=100)
    calorie_amount = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
