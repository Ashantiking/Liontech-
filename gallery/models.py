
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here


# class Category(models.Model):
#    name = models.CharField(max_length=255)

#    def __str__(self):
#        return self.name

#    def get_absolute_url(self):
#        return reverse('gallery')


class Gallery(models.Model):
    image_url = models.CharField(max_length=2085)
    title = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
    #category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery-detail')
