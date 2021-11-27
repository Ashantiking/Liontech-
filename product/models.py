from io import BytesIO
from PIL import Image

from django.core.files import File


#from django.Acheamponginc import File
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
#from blog.models import Category
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here


class Product(models.Model):
    #category = models.ManyToManyField(Category, related_name='product')
    image_url = models.CharField(max_length=2086)
    image_url_1 = models.CharField(max_length=2086)
    image_url_2 = models.CharField(max_length=2086)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    stocks = models.IntegerField()
    sold = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    discription = models.TextField()

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk
                                          })

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'pk': self.pk
                                              })


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}of{self.product.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('products')
