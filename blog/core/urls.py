from django.urls import path
from . import views

urlpatterns = [
    path('',views.adao,name='home'),
    path('adao',views.adao, name="adao"),
    path('eu',views.eu, name="eu"),
    path('blog', views.blog, name="blog"),
    path('projetos',views.projetos),
    path('post/<slug:slug>',views.post),
]
