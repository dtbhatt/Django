from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User

def index(request):
    return render(request, 'logreg/index.html')

def success(request):
    if "userID" in request.session:
        context = {
            "user":User.objects.get(id=request.session["userID"])
        }
        return render(request, 'logreg/success.html', context)
    else:
        messages.add_message(request, messages.ERROR, "Must be a Registered User!")
        return redirect('/')

def login(request):
    errors = User.objects.validlogin(request.POST)
    if len(errors) == 0:
        # request.session["firstName"] = request.POST["firstName"]
        # set id in session
        return redirect('/success')
    
    for error in errors:
        messages.error(request, error) 

    return redirect('/')

def register(request):
    res = User.objects.validregister(request.POST)
    if res["status"]:
        request.session["firstName"] = request.POST["firstName"]
        # set id in session
        return redirect('/success')
    
    for error in res["data"]:
        messages.error(request, error) 


    return redirect('/')


# Create your views here.
