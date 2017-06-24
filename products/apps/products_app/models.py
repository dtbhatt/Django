from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    category = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
