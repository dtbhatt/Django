from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def testimony(request):
    return render(request, 'testimonials.html')
# Create your views here.
