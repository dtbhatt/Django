from django.shortcuts import render, redirect

from .models import Book

def index(request):
    context = {
        "books":Book.objects.all()
    }
    return render(request, 'fsbooks/index.html', context)

def show(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')
# Create your views here.
