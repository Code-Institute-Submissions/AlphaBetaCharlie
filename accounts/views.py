from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductType
from cart import contexts
# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")

def how_to(request):
    """A view that displays the how_to page"""
    return render(request, "how_to.html")

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    # alpha_list = ProductType.objects.get_user_alphas(request.user.id)

    consumed_alpha_list = Product.objects.filter(consumed_by=request.user.id).filter(status='consumed')
    consumed_alpha_price_list = []
    incart_alpha_price_list = []
    for alpha in consumed_alpha_list:
        consumed_alpha_price_list.append(alpha.type.price)

    cart_contents = contexts.cart_contents(request)
    for cart_item in cart_contents['subscription_cart_items']:
            incart_alpha_price_list.append(cart_item['product'].price)

    alpha_types_list = ProductType.objects.filter(base__name='alpha')
    for alpha in alpha_types_list:
        if(alpha.price in consumed_alpha_price_list):
            alpha.status='consumed'
            alpha.image = alpha.image_consumed
            alpha.children = Product.objects.filter(parent=consumed_alpha_list[consumed_alpha_price_list.index(alpha.price)].id)
        elif (alpha.price in incart_alpha_price_list):
            alpha.status='incart'
            alpha.image = alpha.image_available
        else:
            alpha.status='available'
            alpha.image = alpha.image_available
    print("HERE now rendering")
    print(request)
    print(alpha_types_list)
    return render(request, 'profile.html',{"alpha_list": alpha_types_list})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)

