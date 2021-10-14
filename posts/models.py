from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.


class User(models.Model):
    email: models.EmailField(unique=True)
    password: models.CharField(max_length=100)

    firts_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField()

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
