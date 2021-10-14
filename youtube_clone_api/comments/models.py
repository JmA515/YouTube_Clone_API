from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Comment(models.Model):
    body = models.CharField(max_length=200)
    videoId = models.CharField(max_length=50)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

class Reply(models.Model):
    body = models.CharField(max_length=200)
    commentId = models.ForeignKey(
        Comment, on_delete=models.CASCADE)