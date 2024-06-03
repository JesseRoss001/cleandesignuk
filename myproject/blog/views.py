from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post

def index(request):
    """
    View function for the blog index page, which lists posts.
    Allows for searching within titles or content of the posts.
    """
    query = request.GET.get('q')
    if query:
        # Filters posts based on a search query, ignoring case, in both title and content
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-updated_at')
    else:
        # Retrieves all posts and orders them by 'updated_at' date in descending order
        posts = Post.objects.all().order_by('-updated_at')
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'Blog'})

def blog_detail(request, pk):
    """
    Detailed view for a single post, identified by its primary key (pk).
    Uses get_object_or_404 to return the post or raise a 404 error if not found.
    """
    post = get_object_or_404(Post, pk=pk)  # Retrieves the post by ID or raises HTTP 404 if not found
    return render(request, 'blog/blog_detail.html', {'post': post})
