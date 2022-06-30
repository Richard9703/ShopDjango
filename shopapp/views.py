from django.shortcuts import render
from .models import Collection, Product

# Create your views here.
def product_list(request, collection_slug=None):
    collection = None
    collections = Collection.objects.all()
    products = Product.objects.filter(available=True)
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collection=collection)
    return render(request, "product/list.html", {'collection': collection, 'collections': collections, 'products': products})

def product_detail(request):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "about.html",)    
