from django.db import models
from django.utils import timezone
import gfm
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.title

    def content_markdown(self):
        return gfm.markdown(self.content)
