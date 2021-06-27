from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name="topics", on_delete=models.CASCADE)

class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name="+", on_delete=models.CASCADE)
