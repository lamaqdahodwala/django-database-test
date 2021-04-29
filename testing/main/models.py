from django.db import models
# Create your models here.

class Post(models.Model): 
    title = models.CharField(max_length=200)
    body = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
