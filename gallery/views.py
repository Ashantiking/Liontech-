
from django.db import models
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Gallery  # , Category
from .forms import GalleryForm, EditForm
# Create your views here.


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    ordering = ['-publication_date']


# def CategoryView(request, cats):
#    category_gallery = Gallery.objects.filter(category=cats)
#    return render(request, 'categories.html', {'cats': cats.title(), 'category_gallery': category_gallery})


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery/gallery_details.html'


class AddGalleryView(CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'gallery/add_gallery.html'


# class AddCategoryView(CreateView):
#    model = Category
    #form_class = PostForm
#    template_name = 'add_category.html'
#    fields = '__all__'


class UpdateGalleryView(UpdateView):
    model = Gallery
    form_class = EditForm
    template_name = 'gallery/update_gallery.html'


class DeleteGalleryView(DeleteView):
    model = Gallery
    template_name = 'gallery/delete_gallery.html'
    success_url = reverse_lazy('blog')
