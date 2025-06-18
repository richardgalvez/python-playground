from django.http import request
from django.shortcuts import render
from .models import Post


# Create your views here.
def home():
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})
