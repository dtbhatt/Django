from django.shortcuts import render, redirect

def index(request):
    return render(request, 'disninja/index.html')

def ninja(request):
    image = "tmnt.png"
    context = {
        "image":image
    }
    return render(request, 'disninja/ninja.html', context)

def show(request, ninjacolor):
    
    if ninjacolor=="blue":
        image = "donatello.jpg"
    elif ninjacolor == "red":
        image= "leonardo.jpg"
    elif ninjacolor == "green":
        image= "michelangelo.jpg"
    elif ninjacolor == "blue":
        image = "raphel.jpg"
    else:
        image = "notapril.jpg"
    context = {
        "image": image
    }
    return render(request, 'disninja/ninja.html', context)
# Create your views here.

