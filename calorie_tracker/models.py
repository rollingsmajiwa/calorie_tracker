from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class FoodItem(models.Model):
    title = models.CharField(max_length=100)
    calorie_amount = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
