from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html
from django.urls import reverse

from .models import Product, Product_imgs, Customer, Cart, order_placed

# Inline admin for Product Images
class ProductImagesInline(GenericTabularInline):
    model = Product_imgs
    extra = 1  # Number of empty image fields to show

# Admin for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'rating', 'created_at')  # Fields to display in admin list view
    inlines = [ProductImagesInline]  # Add inline images for products


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'name', 'locality', 'city', 'zipcode', 'state')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product_id', 'quantity')

    def product_id(self, obj):
        return obj.product.id

        product_id.short_description = 'Product ID'  
    
@admin.register(order_placed)
class order_placedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'status')
    
    def customer_info(self, obj):
        link = reverse('admin:app_customer_change', args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer)

    def product_info(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product)