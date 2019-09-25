from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from products.views import check_subscription
# Create your views here.

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_subscription_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    # quantity = int(request.POST.get('quantity'))
    # default quantity set to 1
    # quantity = 1

    subscription_cart = request.session.get('subscription_cart', {})
    subscription_cart[id] = 1
    #     cart[id] = quantity
    # else:
    #     cart[id] = cart.get(id, quantity)

    request.session['subscription_cart'] = subscription_cart
    print(request.session['subscription_cart'])
    return redirect(reverse('profile'))


@login_required
@user_passes_test(check_subscription, login_url='/accounts/profile/', redirect_field_name=None)
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    # quantity = int(request.POST.get('quantity'))
    # default quantity set to 1
    quantity = 1

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = quantity
    else:
        cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(reverse('products'))
    # return HttpResponseRedirect("request.path_info")


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """
    Remove an id from the cart
    """
    cart = request.session.get('cart', {})
    if(id in cart):
        cart.pop(id)
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_subscription_from_cart(request, id):
    """
    Remove an id from the cart
    """
    subscription_cart = request.session.get('subscription_cart', {})
    if(id in subscription_cart):
        subscription_cart.pop(id)
    request.session['subscription_cart'] = subscription_cart

    return redirect(reverse('view_cart'))