from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)