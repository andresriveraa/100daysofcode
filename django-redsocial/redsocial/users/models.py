from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    image = models.ImageField(height_field=300, width_field=None)
    wePage = models.URLField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.user.username

