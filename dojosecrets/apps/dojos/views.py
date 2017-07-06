# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect 

from django.contrib import messages

from .models import User, Post

def index(request):
    return render(request, 'dojos/index.html')

def secrets(request):
    if "fName" in request.session:
        context = {
            "user":User.objects.get(firstName=request.session["fName"])
        }
        return render(request, 'dojos/secrets.html', context)
    else:
        messages.add_message(request, messages.ERROR, "Must be a Registered User!")
        return redirect('/')

# def popular(request):
#      = User.objects.get(id=request.session['id'])
#      = Post.objects.annotate(num_likes=Count('all_liked')).order_by('-id')
#     context = {'secretList':,
#                 "userInstance":}
#     return render(request, 'dojos/popular')

def register(request):
    res = User.objects.validRegister(request.POST)
    if res["status"]:
        request.session["fName"] = request.POST["firstName"]
        # set id in session
        return redirect('/secrets')
    
    for error in res["data"]:
        messages.error(request, error) 
    return redirect('/')

def login(request):
    print "Befoere request.post"
    print request.POST['email']
    print "after request.post"
    postData = {
        "email": request.POST["email"]

    }
    errors = User.objects.validLogin(postData)
    if len(errors) == 0:
        request.session["fName"] = request.POST["firstName"]
        return redirect('/secrets')

    for error in errors:
        messages.error(request, error) 
    return redirect('/')
    
def post(request):
    return redirect('/secrets')

def postDisplay(reqeuset):
    User.objects.get(id=request.session["id"])
    Post.objects.all().order_by('-id')[:10]
    return redirect('/secrets') 

# def liked(request):
#     return redirect('/secrets')

# def likeHelper(request, id)
#     user = Post.objects.get(id=id)
#      = User.objects.get(id=request.session['id'])
#     post.all_likes.add(user)
#     return None

# def delete(request):
#     Post.objects.get(id=id).delete()
#     return redirect('/secrets')








# Create your views here.
