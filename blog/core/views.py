from django.shortcuts import render
from .models import Post
# Create your views here.


def home(request):
    return render(request, "home.html",{ "posts": Post.objects.order_by('-created_at')})
