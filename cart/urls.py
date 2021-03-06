from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart, remove_from_cart, add_subscription_to_cart, remove_subscription_from_cart

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/product/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^add/subscription/(?P<id>\d+)', add_subscription_to_cart, name='add_subscription_to_cart'),
    # url(r'^adjust/(?P<id>\d+)', adjust_cart, name='adjust_cart'),
    url(r'^remove/product/(?P<id>\d+)', remove_from_cart, name='remove_from_cart'),
    url(r'^remove/subscription/(?P<id>\d+)', remove_subscription_from_cart, name='remove_subscription_from_cart'),
]