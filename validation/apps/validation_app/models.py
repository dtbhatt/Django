from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def emailvalid(self, post):
        email = post["email"]
        errors = []

        if len(email)<2:
            errors.append("Too short")
        
        if len(email)>15:
            errors.append("Too long")
        
        exist = User.objects.filter(email=email).exists()
        if exist:
            errors.append("Already exists")
        
        if not errors:
            email = User.objects.create(email=email)
            return { "status": True, "data": email}
        else:
            return {"status": False, "data": errors}



class User(models.Model):
    email = models.CharField(max_length=26)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

# Create your models here.
