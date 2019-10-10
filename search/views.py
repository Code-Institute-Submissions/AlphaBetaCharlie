from django.shortcuts import render
from products.models import Product
from .models import ProductBase

# Create your views here.

def do_search(request):
    products = ProductBase.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})