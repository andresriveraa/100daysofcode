from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """proxy model that extends """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interest = models.TextField(max_length=100)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='user/picture',
                              blank=True,
                              null=True
                              )
    wePage = models.URLField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.user.username

