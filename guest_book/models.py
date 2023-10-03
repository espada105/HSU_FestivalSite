from django.db import models
from django.utils import timezone

# Create your models here.

class Comments(models.Model):
    comment = models.TextField(max_length=150, null=False, default="")
    nickname = models.CharField(max_length=30, default="")
    created = models.DateTimeField(auto_now_add=True)