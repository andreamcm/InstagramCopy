from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Post model
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    posted_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, 'Like')

# PostLikes model
class Postlikes(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
