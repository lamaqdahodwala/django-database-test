from django.db import models

# Create your models here.

class Question(models.Model):
    q = models.TextField()

    def __str__(self):
        return self.q

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text = models.TextField()
    votes = models.IntegerField(default=0)