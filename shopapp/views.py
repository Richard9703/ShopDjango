# from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.
# class ProductList(ListView, collection_slug=None):
#     collection = None
#     collections = Collection.objects.all()
#     products = Product.objects.filter(available=True)
#     if collection_slug:
#         collection = get_object_or_404(Collection, slug=collection_slug)
#         products = products.filter(collection=collection)
#     # return render(request, "list.html", {'collection': collection, 'collections': collections, 'products': products})

# class ProductDetail(ListView):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     # return render(request, "detail.html")   
# 
class ProductList(generic.ListView):
    model = Product
    queryset = Product.objects.filter(available=1).order_by('-created')
    template_name = 'index.html'
    paginate_by = 6



