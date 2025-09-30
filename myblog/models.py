from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
        title = models.CharField(max_length=100)
        body = models.CharField(max_length=100000)
        updated_at = models.DateTimeField(auto_now=True)
        created_date = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey(User, on_delete=models.CASCADE)

# database for comment section with foreign  key 
class comment(models.Model):
        text = models.CharField(max_length=300)
        comment_date = models.DateTimeField(auto_now_add=True)
        pOst = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
        author = models.ForeignKey(User, on_delete=models.CASCADE)
## related name (reverse)s