from django.shortcuts import render
from .models import People

def index(request):
    People.objects.create(first_name="Dhaval", last_name="Bhatt")
    people = People.objects.all()
    print (people)
    return render(request, 'index.html')


# Create your views here.
