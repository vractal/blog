from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid
import gfm
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True,default=uuid.uuid4) 
       #published_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.title

    def content_markdown(self):
        return gfm.markdown(self.content)
