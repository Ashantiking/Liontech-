from django.urls import path
from django.views.generic.edit import UpdateView
from .views import AddPostView, BlogView, ArticleDetailView,  AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('add_category', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
