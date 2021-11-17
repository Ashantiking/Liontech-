
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product')


class Product(models.Model):
    image_url = models.CharField(max_length=2085)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField()
    descriptions = models.TextField()
    purchase_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='product_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('product-detail', args=(str(self.id)))


#from django.conf import settings
#from django.db import models

# Create your models here.


# class Item(models.Model):
#    title = models.CharField(max_length=100)
#    price = models.FloatField()
#
#    def __str__(self):
#        return self.title


# class OrderItem(models.Model):
#    Item = models.ForeignKey(Item, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.title


# class Order(models.Model):
#    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    items = models.ManyToManyField(OrderItem)
#    start_date = models.DateTimeField(auto_now_add=True)
#    ordered_date = models.DateTimeField()
#    ordered = models.BooleanField(default=False)

#    def __str__(self):
#        return self.user.username
