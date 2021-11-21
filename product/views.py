from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product  # , Categorie
from .forms import ProductForm, EditForm
from django.http import HttpResponseRedirect
# Create your views here.


def LikeView(request, pk):
    product = get_object_or_404(Product, id=request.POST.get('product_pk'))
    product.like.add(request.user)
    return HttpResponseRedirect(reverse('product-detail', args=[str(pk)]))


class ProductView(ListView):
    model = Product
    template_name = 'products/product.html'
    ordering = ['-date_added']


def Categorie(request, cat):
    categorie_product = Product.objects.filter(categorie=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'categorie_product': categorie_product})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    success_url = reverse_lazy('product')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(ProductDetailView, self).get_context_data()

        stuff = get_object_or_404(Product, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/add_product.html'
    success_url = reverse_lazy('product')


# class AddCategorieView(CreateView):
#    model = Categorie
    #form_class = ProductForm
#    template_name = 'add_category.html'
#    fields = '__all__'


class UpdateProductView(UpdateView):
    model = Product
    form_class = EditForm
    template_name = 'product/update_product.html'
    success_url = reverse_lazy('product')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product')
