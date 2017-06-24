from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Interest(models.Model):
    interest = models.CharField(max_length=100)
    users = models.ManyToManyField(User)



# Create your models here.
