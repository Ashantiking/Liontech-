from django.urls import path
from django.views.generic.edit import UpdateView
from .views import ProductView, ProductDetailView, AddProductView, UpdateProductView, DeleteProductView, AddCategoryView, CategoryView, LikeView


urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:pk>/remove',
         DeleteProductView.as_view(), name='delete_product'),
    #path('add_categorie', AddCategorieView.as_view(), name='add_categorie'),
    #path('categorie/<str:cats>', CategorieView, name='categorie'),
    path('like/<int:pk>', LikeView, name='like_product'),
]
