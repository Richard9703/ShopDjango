from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)
    

def product(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        try: 
            customer = request.user.customer
        except: 
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')

    context = {'product': product}   
    return render(request, 'shop/product.html', context)


def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    context = {'order': order}
    return render(request, 'shop/cart.html', context)    


