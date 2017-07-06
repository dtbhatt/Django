# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validRegister(self, postData):
        firstName = postData["firstName"]
        lastName = postData["lastName"]
        email = postData["email"]
        password = postData["password"]
        confirmPassword = postData["confirmPassword"]

        errors = []

        if len(firstName) < 1:
            errors.append("First Name cannot be empty")
        elif not firstName.isalpha():
            errors.append("First Name can only contain leters")
        
        if len(lastName) < 1:
            errors.append("Last Name cannot be empty")
        elif not lastName.isalpha():
            errors.append("Last Name can only contain leters")
        
        if len(email) < 1:
            errors.append("Email cannot be empty")
        elif not EMAIL_REGEX.match(email):
            errors.append("Email is not valid")
        
        if len(password) < 1:
            errors.append("Password cannot be empty")
        elif password != confirmPassword:
            errors.append("Password and Confirm password has to be same")
        
        if len(confirmPassword) < 1:
            errors.append("Confirm password cannot be empty")
        elif confirmPassword != password:
            errors.append("Password and Confirm password has to be same")

        exist = User.objects.filter(email=email).exists()

        if exist:
            errors.append("Already exists")
        
        if not errors:
            # myString=""
            mypassword = password.encode()
            hashed = bcrypt.hashpw(mypassword,bcrypt.gensalt())
            # myString = hashed           
            user = User.objects.create(firstName=firstName, lastName=lastName, email=email, password=hashed)
            return {"status": True, "data": user}
        else:
            return {"status": False, "data": errors}     
    
    def validLogin(self, postData):
        email = postData["email"]
        print postData["email"]
        password = postData["password"]
        errors = []

        try:
            user_list = User.objects.filter(email=email)              
            if not user_list:
                errors.append("Invalid email or invalid password")
            elif user_list[0].password != password:
                errors.append("Invalid password")

        except: 
            errors.append("Invalid email and invalid password!")

        return errors


class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, related_name="all_post")
    likes = models.ManyToManyField(User, related_name="all_likes")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)




# Create your models here.
