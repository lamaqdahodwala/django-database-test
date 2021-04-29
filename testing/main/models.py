from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model): 
    body = models.TextField()
    title = models.CharField(max_length=200)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
