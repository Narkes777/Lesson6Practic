from cgi import print_exception
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Car(models.Model):
    lada = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    manufacturer = models.ForeignKey('manufacturer', on_delete=models.CASCADE)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)