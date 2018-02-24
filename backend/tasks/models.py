from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
