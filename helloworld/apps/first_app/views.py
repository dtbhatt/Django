from django.shortcuts import render

def index(request):
    print "Hello world!"
    return render(request, 'first_app/index.html')

# Create your views here.
