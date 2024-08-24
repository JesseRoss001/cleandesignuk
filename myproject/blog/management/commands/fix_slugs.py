from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Populate slugs for posts that are missing them'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        for post in posts:
            if not post.slug:
                post.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated slugs'))
