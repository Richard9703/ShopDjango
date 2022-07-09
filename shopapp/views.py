from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


