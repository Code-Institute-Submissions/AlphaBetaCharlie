from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product, ProductType
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
        if request.method=="POST":
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.save()


                cart = request.session.get('cart', {})
                subscription_cart = request.session.get('subscription_cart', {})
                total = 0

                for id, quantity in cart.items():
                    product = get_object_or_404(Product, pk=id)
                    temp = product.type.id
                    producttype = get_object_or_404(ProductType, pk=temp)
                    total += quantity * product.type.price
                    order_line_item = OrderLineItem(
                        order = order,
                        product = product,
                        type = producttype,
                        quantity = quantity
                        )
                    order_line_item.save()

                for id, quantity in subscription_cart.items():
                    product = get_object_or_404(ProductType, pk=id)
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order = order,
                        type = product ,
                        quantity = quantity
                        )
                    order_line_item.save()


                try:
                    customer = stripe.Charge.create(
                        amount = int(total * 100),
                        currency = "EUR",
                        description = request.user.email,
                        card = payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!")

                if customer.paid:
                    messages.error(request, "You have successfully paid")

                    for id, quantity in cart.items():
                        product = get_object_or_404(Product, pk=id)
                        try:
                            #mark current product as consumed with consumed_by, create new set of children, beta and charlie
                            consumed_product = Product.objects.consume(product, request.user.id)
                            new_children = Product.objects.create_all_available_children(product, request.user.id)
                        except Exception as e:
                            messages.error(request, "Payment success but object assignment unsuccessful. Please contact us.")

                    for id, quantity in subscription_cart.items():
                        product = get_object_or_404(ProductType, pk=id)
                        try:
                            #create an alpha with user as parent, create other children of same value - beta and charlie
                            new_alpha = Product.objects.create_consumed_alpha(product, request.user.id)
                            print(new_alpha)
                            new_children = Product.objects.create_all_available_children(new_alpha, request.user.id)
                        except Exception as e:
                            messages.error(request, "Payment success but object assignment unsuccessful. Please contact us.")

                    request.session['cart'] = {}
                    request.session['subscription_cart'] = {}

                    return redirect(reverse('products'))

                else:
                    messages.error(request, "Unable to take payment")
            else:
                print(payment_form.errors)
                messages.error(request, "We were unable to take a payment with that card!")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

        return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
