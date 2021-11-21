
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vendor
from .forms import VendorForm, EditForm
# Create your views here.
# Create your views here.


# def become_vendor(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#
#        if form.is_valid:
#            user = form.save()
#            login(request, user)

#            vendor = Vendor.objects.create(name=user.username, created_by=user)
#            return redirect('vendor')
#        else:
#            form = UserCreationForm()

#    return render(request, 'vendor/become_vendor.html', {})


# Create your views here.


class VendorView(ListView):
    model = Vendor
    template_name = 'vendor/vendor.html'
    ordering = ['-name']


class AddVendorView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'vendor/become_vendor.html'
    success_url = reverse_lazy('vendor')


class UpdateVendorView(UpdateView):
    model = Vendor
    form_class = EditForm
    template_name = 'vendor/update_vendor.html'
    success_url = reverse_lazy('vendor')


class DeleteVendorView(DeleteView):
    model = Vendor
    template_name = 'vendor/delete_post.html'
    success_url = reverse_lazy('vendor')
