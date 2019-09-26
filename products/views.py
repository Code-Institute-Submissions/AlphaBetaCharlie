from django.shortcuts import render
from .models import Product, ProductBase
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.contrib import messages
# Create your views here.
def all_products(request):

    final_products = Product.objects.none()

    if request.user.is_authenticated:
        # getting all alpha products consumed by the user, used to retrive same value B and C
        alpha_products = Product.objects.filter(type__base__name='alpha', consumed_by=request.user.id)
        # all products but not alpha & not created by the user & status = available
        products = Product.objects.exclude(type__base__name="alpha").exclude(created_by=request.user.id).filter(status='available')

# for future use to hold items in cart while restricting others from entering same items to cart. Line 27 below needs to be uncommented as well
# select_for_update(Sof=('self',), skip_locked=True).
        #if user has consumed an alpha
        if len(alpha_products)>0:
            #for each alpha subscribed by the user, get one B and one C of the same value, sorted by created_at, add it to final_products
            for alpha in alpha_products:
                for base in get_all_productbases():
                    base_products = products.filter(type__price=alpha.type.price).filter(type__base__id=base.id).order_by('created_at')[0:1]
                    final_products = final_products | base_products
                    # Product.objects.filter(pk__in=base_products).update(status='held', updated_at=timezone.now())

            #setting a variable for each product to understand its cart_presence
            cart = request.session.get('cart', {})
            for p in final_products:
                set_cart_presence(cart,p)
            return render(request, "products_user.html", {"products": final_products})

        #if user has not consumed alpha, take him to generic products page when he will be redirected to buy alphas when he tries to buy B and C
        else:
            products = Product.objects.exclude(type__base__name='alpha')
            return render(request, "products_all.html", {"products": products})
    else:
        products = Product.objects.exclude(type__base__name='alpha')
        return render(request, "products_all.html", {"products": products})


# def clear_held_items():

# check whether a user has bought any product from our store
def check_subscription(user):
    user_products = Product.objects.filter(consumed_by=user.id)
    if len(user_products)>0:
        return True
    else:
        return False

#checks if product is in cart
def check_product_in_cart(cart, id):
    if str(id) in cart:
        return True
    else:
        return False

#sets cart presence of a product based on whether it is present in cart, used to set the button to disabled and added to cart
def set_cart_presence(cart, product):
    if check_product_in_cart(cart,product.id):
        product.cart_presence=True
    else:
        product.cart_presence=False

#gets all the productbase entries
def get_all_productbases():
    return ProductBase.objects.all()