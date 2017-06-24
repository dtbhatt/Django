from django.shortcuts import render

from .models import Product

def index(request):
    Product.objects.create(name="iPhone", description="Smart phone", cost=13, price=770, weight=2, category="It's sometimes stupid")
    product = Product.objects.all()
    print product
    for pro in product:
        print pro.name
  
    return render(request, 'products_app/index.html')
# Create your views here.s
