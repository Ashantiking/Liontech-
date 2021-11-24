from django.contrib import admin
from .models import Order, OrderProduct, Product

admin.site.register(Product),
admin.site.register(OrderProduct),
admin.site.register(Order),
