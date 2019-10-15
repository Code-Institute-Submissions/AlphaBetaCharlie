from django.shortcuts import render
from products.models import Product
from django.db.models import Q

# Create your views here.

def do_search(request):
    products = Product.objects.filter( Q (created_by__username__icontains=request.GET['q']) | Q (type__name__icontains=request.GET['q']) )
    return render(request, "products_user.html", {"products":products})




