from django.urls import path
from . import views

urlpatterns = [
    path('',views.adao,name='home'),
    path('adao',views.adao, name="adao"),
    path('blog', views.blog, name="blog"),
    path('post/<slug:slug>',views.post)
]
