from django.shortcuts import render
from .models import Post, Tag
from django.http import HttpResponseNotFound, Http404
# Create your views here.



def adao(request):
    try:
        tag = Tag.objects.get(name='adao')
    except:
        tag = Tag.objects.create(name="adao",description="adao")
    return render(request, "home.html",{ "posts": Post.objects.filter(tags=tag).order_by('-created_at'),
                                        "project_menu":Post.objects.get(slug="project-menu-markdown")})

def blog(request):
    try:
        tag = Tag.objects.get(name='blog')
    except:
        tag = Tag.objects.create(name="blog",description="blog")

    #posts = Post.objects.filter(tags=tag).order_by('-created_at')
    posts = Post.objects.all().exclude(slug="project-menu-markdown").order_by('-created_at')

    return render(request, "blog.html",{'posts':posts})


def eu(request):
    return render(request,"eu.html")

def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        try:
            tag = Tag.objects.get(name='adao')
        except:
            tag = Tag.objects.create(name="adao",description="adao")
        if Tag.objects.get(name='adao') in post.tags.all():
            template = "home.html"
        else:
            template = "blog.html"
        return render(request,template, {'posts':[post], "project_menu":Post.objects.get(slug="project-menu-markdown")})
    except:
        raise Http404


def projetos(request):
    return render(request, template_name="projetos.html")