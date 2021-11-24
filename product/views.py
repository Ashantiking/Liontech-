from __future__ import unicode_literals

from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
#from shopping_cart.models import Order
from .models import Product, OrderProduct, Order
#from category.models import Category
from .forms import ProductForm, EditForm
# Create your views here.


# def product_list(request):
#    object_list = Product.objects.all()
#    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered)
#    current_order_products = []
#    if filtered_orders.exists():
#        user_order = filtered_orders[0]
#        user_order_items = user_order.all()
#        current_order_products = [product.product for product in product user_order_items]

#    context = {
#        'object_list': object_list,
#        'current_order_products': current_order_products
#    }
#    return render(request, "products/pro", context)

class ProductView(ListView):
    model = Product
    template_name = 'product/product.html'
    ordering = ['-date_added']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_product = OrderProduct.objects.create(product=product)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
# check if the order item is in the order
        if order.product.filter(product__pk=product.pk).exists():
            order_product.quantity += 1
            order_product.save()

        else:
            order_date = timezone.now()
            order = Order.objects.create(
                user=request.user, ordered_date=order_date)
            order.product.add(order_product)
        return redirect("product", kwargs={int: pk})


class NewProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/new_product.html'


# class AddCategoryView(CreateView):
    #model = Category
    #form_class = ProductForm
    #template_name = 'add_category.html'
    #fields = '__all__'


class UpdateProductView(UpdateView):
    model = Product
    form_class = EditForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('product')


class UpdateAddToCartView(UpdateView):
    model = Product
    form_class = EditForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('product')


def wishlist(request):
    return render(request, 'product/wishlist.html', {})
