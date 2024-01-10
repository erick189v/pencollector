from django.db import models

# Create your models here.
class Pen(models.Model):
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    length = models.IntegerField()