from django.urls import path
from django.views.generic.edit import UpdateView
from .views import VendorView, AddVendorView, DeleteVendorView

urlpatterns = [
    path('', VendorView.as_view(), name='vendor'),
    path('add_vendor/', AddVendorView.as_view(), name='add_vendor'),
    path('vendor/<int:pk>/remove', DeleteVendorView.as_view(), name='delete_vendor'),
]
