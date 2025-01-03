from django.contrib import admin
from .models import Featured_product, Product, Product_imgs

# Register your models here.
@admin.register(Featured_product)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'rating', 'description', 'images', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'rating', 'description', 'images', 'created_at')

@admin.register(Product_imgs)
class Product_imgsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'images', 'created_at', 'updated_at')