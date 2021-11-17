from django.urls import path
from django.views.generic.edit import UpdateView
# , AddCategoryView, CategoryView
from .views import AddGalleryView, GalleryView, GalleryDetailView,  AddGalleryView, UpdateGalleryView, DeleteGalleryView

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery'),
    path('article/<int:pk>', GalleryDetailView.as_view(), name='gallery-detail'),
    path('add_post/', AddGalleryView.as_view(), name='add_gallery'),
    path('article/edit/<int:pk>', UpdateGalleryView.as_view(), name='update_gallery'),
    path('gallery/<int:pk>/remove',
         DeleteGalleryView.as_view(), name='delete_gallery'),
    #path('add_category', AddCategoryView.as_view(), name='add_category'),
    #path('category/<str:cats>', CategoryView, name='category'),
]
