from __future__ import unicode_literals

import os, binascii
from django.shortcuts import render, redirect

def index(reqeust):

    if 'randomword' in request.session:
        pass
    elif 'attempt' in request.session:
        pass
    else:
        request.session['attempt'] = 1
        request.session['randomword'] = binascii.b2a_hex(os.urandom(15))
    return render(request, 'index.html')

def generate(request):
    request.session['attempt'] += 1
    request.session['randomword'] = binascii.b2a_hex(os.urandom(15))
    return redirect('/')

# Create your views here.
