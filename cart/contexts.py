from django.shortcuts import get_object_or_404
from products.models import Product, ProductType


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})
    subscription_cart = request.session.get('subscription_cart', {})

    cart_items = []
    subscription_cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        print(product)
        total +=  product.type.price
        cart_items.append({'id':id, 'quantity': 1, 'product': product,})
        product_count += 1

    for id, quantity in subscription_cart.items():
        product = get_object_or_404(ProductType, pk=id)
        print(product)
        total +=  product.price
        subscription_cart_items.append({'id':id, 'quantity': 1, 'product': product,})
        product_count += 1


    return { 'cart_items': cart_items, 'subscription_cart_items': subscription_cart_items, 'total': total, 'product_count': product_count}