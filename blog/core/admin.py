from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag)
