from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=128, default="empty")
    created = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Follower(models.Model):
    follows = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="%(class)s_foo")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="%(class)s_bar")
