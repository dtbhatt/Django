from django.shortcuts import render, redirect

from django.contrib import messages

from .models import User, Secret

def index(request):
    return render(request, 'dojosec/index.html')

def secrets(request):
    if "id" in request.session:
        allsecrets = Secret.objects.all().order_by('-id')[:5]
        context = {
            "user":User.objects.get(id=request.session['id']),
            "secrets":allsecrets
        }
        # return render(request, 'dojosec/secrets.html', context)
        return render(request, 'dojosec/secrets.html', context)
    else:
        messages.add_message(request, messages.ERROR, "Must be a Registered User!")
        return redirect('/')

def popular(request):
    return render(request, 'dojosec/popular.html')

def login(request):
    res = User.objects.validlogin(request.POST)
    if res["status"]:
        # set id in session
        request.session["id"] = res["data"].id
        return redirect('/secrets')
    
    for error in res["data"]:
        messages.error(request, error) 

    return redirect('/')

def register(request):
    res = User.objects.validregister(request.POST)
    if res["status"]:
        # set id in session
        request.session["id"] = res["data"].id
        return redirect('/secrets')
    
    for error in res["data"]:
        messages.error(request, error) 

    return redirect('/')

def process(request):
    result = Secret.objects.validPost(request.POST['secrets'], request.session['id'])
    if result[0]: 
        messages.info(request, result[1])
        return redirect('/secrets')
    messages.error(request, result[1])
    return redirect('/secrets')

def newlike(request, id):
    Secret.objects.newlike(id, request.session['id'])
    return redirect('/secrets')

def logout(request):
    request.session.pop('id')
    return redirect('/')


# Create your views here.
 