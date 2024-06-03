from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Use TextField for rich text content
    image = CloudinaryField('image', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates each time the object is saved

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Assuming the url name for viewing a post is 'post_detail' and uses the post's ID
        return reverse('post_detail', args=[str(self.id)])
