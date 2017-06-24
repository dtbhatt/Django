from django.shortcuts import render, redirect 
from django.contrib import messages

from .models import User


def index(request):  
    return render(request, 'validation_app/index.html')

def show(request):
    if request.method == "POST":
        res = User.objects.emailvalid(request.POST)
        if res['status']:
            email = res['data'].email
            messages.success(request, "The username {} is valid".format(email))
            return redirect('/success')
        else:
            for error in res['data']:
                messages.error(request, "{}".format(error))
            return redirect('/')

def success(request):
    context = {
        "users":User.objects.all()
    }
    return render(request, 'validation_app/success.html', context)

# Create your views here.
