from django.shortcuts import get_object_or_404
from django.urls import resolve
from products.models import Product

def transaction_summary(request):
   allowed_urls = ['products', 'profile','view_cart','checkout']
   current_url = resolve(request.path_info).url_name
   if current_url in allowed_urls and request.user.is_authenticated:
       final_values = Product.objects.get_user_transaction_summary(request.user.id)
       final_values['transaction_summary'] = True
       return final_values
   else:
       return {'transaction_summary': False}