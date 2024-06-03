from django.contrib.sitemaps import Sitemap
from .models import Post  # Adjust the model name based on your actual blog post model

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # Adjust the attribute to your model's last modified timestamp

    def location(self, obj):
        return obj.get_absolute_url()  # Ensure your model has a get_absolute_url() method
