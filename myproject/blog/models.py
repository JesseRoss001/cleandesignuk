from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, editable=False)  # allow null temporarily
    meta_title = models.CharField(max_length=70, blank=True, help_text="Title for SEO (max 70 characters)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="Meta description for SEO (max 160 characters)")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated keywords for SEO")
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
