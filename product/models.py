
#from django.Acheamponginc import File
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
#from blog.models import Category
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
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

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            "pk": self.pk
        })


class OrderProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}of{self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.title

    def get_discount_item_price(self):
        return self.quantity * self.product.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.product.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    checkout_address = models.ForeignKey(
        'CheckoutAddress', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.products.all():
            total += order_item.get_final_price()
        return total


class CheckoutAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
