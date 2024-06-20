# project_gallery/models.py
from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set the field to now every time the object is saved.
    def __str__(self):
        return self.title