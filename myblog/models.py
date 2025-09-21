from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
        title = models.CharField(max_length=100)
        body = models.CharField(max_length=100000)
        updated_at = models.DateTimeField(auto_now=True)
        created_date = models.DateTimeField(auto_now_add=True)

# database for comment section with foreign  key 
class comment(models.Model):
        text = models.CharField(max_length=300)
        comment_date = models.DateTimeField(auto_now_add=True)
        pOst = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
## related name (reverse)s