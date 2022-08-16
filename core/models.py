from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Inventory(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=100)
    Product_qty = models.IntegerField()
