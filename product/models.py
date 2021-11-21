from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from blog.models import Category
# Create your models here.


# class Categorie(models.Model):
#    name = models.CharField(max_length=200)

#    def __str__(self):
#        return self.name

#    def get_absolute_url(self):
#        return reverse('product')


class Product(models.Model):
    image_url = models.ImageField(upload_to=None, height_field=None,
                                  width_field=None, max_length=100, )
    relate_image_url = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=10, max_digits=2)
    discount_price = models.DecimalField(decimal_places=10, max_digits=2)
    quantity = models.FloatField(default=1)
    stock = models.FloatField(default=1)
    sold = models.FloatField()
    category = models.CharField(max_length=200)
    discription = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User, related_name='like_product')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=(str(self.pk)))
