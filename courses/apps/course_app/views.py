from django.shortcuts import render, redirect

from .models import Course

def index(request):
    context = {
        "courses":Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def show(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
        "course":Course.objects.get(id=id)
    }  
    return render(request, 'course_app/destroy.html', context)

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

