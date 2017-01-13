from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here

class User(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name

class blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
