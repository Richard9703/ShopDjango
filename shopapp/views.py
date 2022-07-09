from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'nav.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


