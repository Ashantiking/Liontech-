
from django.urls import path
from django.views.generic.edit import UpdateView
from .views import ProductView, ProductDetailView, NewProductView, UpdateProductView, add_to_cart, wishlist

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product-detail/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
    path('new_product/', NewProductView.as_view(), name='new_product'),
    # path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('product-detail/edit/<int:pk>/',
         UpdateProductView.as_view(), name='update_product'),
    path('wishlist/', wishlist, name='wishlist'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]
