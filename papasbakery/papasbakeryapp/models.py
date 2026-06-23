from django.db import models

# Create your models here.


class Product(models.Model):
    procuct_name = models.CharField(max_length=500)
    product_price = models.Count("figure")


class Allergies(models.Model):
    choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)