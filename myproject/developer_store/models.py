from django.db import models
from cloudinary.models import CloudinaryField

class Template(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

class Component(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
