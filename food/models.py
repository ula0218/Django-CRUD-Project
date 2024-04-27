from django.db import models

# Create your models here.
class Food(models.Model):
    food=models.CharField(max_length = 100)
    price=models.CharField(max_length = 1000000)
    date=models.CharField(max_length = 100)
