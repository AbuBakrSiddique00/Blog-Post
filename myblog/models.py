from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
        title = models.CharField(max_length=100)
        body = models.CharField(max_length=100000)
        updated_at = models.DateTimeField(auto_now=True)
        created_date = models.DateTimeField(auto_now_add=True)
# class comment(models.Model):