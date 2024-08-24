from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
from django.core.paginator import Paginator

def index(request):
    """
    View function for the blog index page, which lists posts.
    Allows for searching within titles or content of the posts.
    """
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-updated_at')
    else:
        posts = Post.objects.all().order_by('-updated_at')

    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_obj': page_obj, 'title': 'Blog'})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
        'meta_title': post.meta_title or post.title,
        'meta_description': post.meta_description,
        'meta_keywords': post.meta_keywords,
    }
    return render(request, 'blog/blog_detail.html', context)
