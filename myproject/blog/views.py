from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post

def index(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts, 'title': 'Blog'})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})