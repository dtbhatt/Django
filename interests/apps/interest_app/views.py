from django.shortcuts import render, redirect

from .models import User, Interest

def index(request):
    User.objects.create(username=request.POST['username'])
    return render(request, 'interest_app/index.html')

def users(request): 
    
    context = {
        "users":User.objects.all()
    }
    return render(request, 'interest_app/users.html', context)

def show(request):
    return render(request, 'interest_app/show.html')

def process(request):
    
    return redirect('/users')
# Create your views here.