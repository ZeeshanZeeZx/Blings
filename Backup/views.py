from django.shortcuts import render
from .models import Featured_product, Product, Product_imgs
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    f_products_details = Featured_product.objects.all()
    return render(request, 'index.html', {'products': f_products_details})

def shop(request):
    shop_products = Product.objects.all()
    paginator = Paginator(shop_products, 4)  # Show 4 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop.html', {'page_obj': page_obj})

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def product_detail(request, id):
    f_products_details = Featured_product.objects.all()

    if id:
        product = Product.objects.get(id=id)
        product_img = Product_imgs.objects.get(id=product.id)
        return render(request, 'product_detail.html', {'product': product, 'f_products': f_products_details, 'product_img': product_img})
        # return render(request, 'product_detail.html', {'product': product, 'f_products': f_products_details})
