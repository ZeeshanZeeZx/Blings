# ------------------------------------6:34 ---------------------------------- 

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Product, Product_imgs
from django.core.paginator import Paginator
from django.contrib.contenttypes.models import ContentType
# from django.http import JsonResponse
from django.views import View
from app.forms import CustomerRegistrationForm, LoginForm, UserPasswordChangeForm, CustomerProfileForm
from django.contrib import messages
from .models import Customer, Cart, Product, order_placed

from random import randint
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    product = Product.objects.order_by('?')[:3]
    return render   (request, 'index.html', {'products': product})

def shop(request):
    shop_products = Product.objects.all()
    paginator = Paginator(shop_products, 12)  # Show 4 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html', {'page_obj': page_obj})

@login_required
def orders(request):
    op = order_placed.objects.filter(user=request.user)
    return render(request, 'orders.html', {'order_placed': op})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 100.00
    totalamount = 0.0
    cart_product = [item for item in Cart.objects.all() if item.user == request.user]
    if cart_product:
        for item in cart_product:
            amount += item.product.price * item.quantity
        totalamount = amount + shipping_amount
    return render(request, 'checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    if not custid:
        return HttpResponse("Customer ID is missing", status=400)

    try:
        customer = Customer.objects.get(id=custid)
        cart = Cart.objects.filter(user=user)
        for item in cart:
            order_placed(user=user, customer=customer, product=item.product, quantity=item.quantity).save()
            item.delete()
        return redirect('orders')  # Named view or URL pattern
    except Customer.DoesNotExist:
        return HttpResponse("Customer does not exist", status=404)

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart/')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 100.00
        # total_amount = 0.0
        cart_product = [item for item in Cart.objects.all() if item.user == user]
        if cart_product:
            for item in cart_product:
                amount += item.product.price * item.quantity
                total_amount = amount + shipping_amount
            return render(request, 'addtocart.html', {'carts': cart, 'amount':amount, 'total_amount': total_amount})
        return render(request, 'emptycart.html')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [item for item in Cart.objects.all() if item.user == request.user]
        for item in cart_product:
            amount += item.product.price * item.quantity
        data = {'quantity': c.quantity,
        'amount':amount,
        'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [item for item in Cart.objects.all() if item.user == request.user]
        for item in cart_product:
            amount += item.product.price * item.quantity
        data = {'quantity': c.quantity,
        'amount':amount,
        'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 100.00
        cart_product = [item for item in Cart.objects.all() if item.user == request.user]
        for item in cart_product:
            amount += item.product.price * item.quantity
        data = {'amount':amount,
        'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    item_already_in_cart = False
    if request.user.is_authenticated:
        item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()

    product_images = Product_imgs.objects.filter(
        content_type=ContentType.objects.get_for_model(Product),
        object_id=product.id
    )
    return render(request, 'product_detail.html', {'product': product, 'product_images': product_images, 'item_already_in_cart': item_already_in_cart})


class CustomerRegistrationView(View):
    def get(self, request):   # This method is to show the form in html
        form = CustomerRegistrationForm()
        return render(request,'register.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have Registered Successfully')
            form.save()
        return render(request,'register.html', {'form': form})

@login_required
def address(request):
    user_address = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', {'user_address':user_address, 'active': 'btn-primary'})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'profile.html', {'form': form, 'active': 'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            state = form.cleaned_data['state']
            reg = Customer(user=usr, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Profile updated successfully')
        return render(request,'profile.html', {'form': form, 'active': 'btn-primary'})
