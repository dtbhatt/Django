from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=250)