from django.db import models

# Create your models here.
class Featured_product(models.Model):
    images = models.ImageField(upload_to="featured_product_imgs/")
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    images = models.ImageField(upload_to="product_imgs/")
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Product_imgs(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_imgs')
    images = models.ImageField(upload_to="product_imgs/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


