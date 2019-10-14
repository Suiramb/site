from django.shortcuts import render, get_object_or_404
from .models import Post
# from .articles import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index_blog.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'show.html', {'post': post})

# Create your views here.
