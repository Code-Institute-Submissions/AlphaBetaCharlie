from django.shortcuts import render
from products.models import Product, ProductBase, ProductType

# Create your views here.

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products_user.html", {"products":products})
