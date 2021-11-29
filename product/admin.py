from django.contrib import admin
from .models import Order, OrderProduct, Product, CheckoutAddress, Payment

admin.site.register(Product),
admin.site.register(OrderProduct),
admin.site.register(Order),
admin.site.register(CheckoutAddress),
admin.site.register(Payment),
