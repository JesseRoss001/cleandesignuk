from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    image = CloudinaryField('image', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title