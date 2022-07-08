from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def register(request):
    return render(request, 'register.html')
