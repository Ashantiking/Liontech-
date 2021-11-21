from django import forms
from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'created_by',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control',  'value': '', 'id': 'liven', 'type': 'hidden'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('name', 'created_by',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control',  'value': '', 'id': 'liven', 'type': 'hidden'}),


        }
