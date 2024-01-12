from django.db import models
from django.urls import reverse

# Create your models here.
class Pen(models.Model):
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    length = models.IntegerField()
    def __str__(self):
        return f'{self.brand} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pen_id': self.id})

