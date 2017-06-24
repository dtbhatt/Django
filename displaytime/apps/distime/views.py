from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        'date':strftime("%B %d, %Y", gmtime()),
        'time':strftime("%H:%M %p", gmtime())
    }
    return render(request, 'distime/index.html', context)

# Create your views here.
