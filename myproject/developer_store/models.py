from django.db import models
from cloudinary.models import CloudinaryField

class Template(models.Model):
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=255, help_text="Short introduction for template, shown on the card.")
    description = models.TextField(help_text="Full description that can include HTML, shown in modal.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

class Component(models.Model):
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=255, help_text="Short introduction for component, shown on the card.")
    description = models.TextField(help_text="Full description that can include HTML, shown in modal.")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
