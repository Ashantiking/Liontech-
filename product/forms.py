from django import forms
from .models import Product  # , Categorie
from blog.models import Category


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'relate_image_url', 'title', 'price', 'discount_price',
                  'quantity', 'stock', 'sold', 'categorie', 'description', ),

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'relate_image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relate Images'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount Price'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity in Stock'}),
            'sold': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity in Sold'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'description': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a Category'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'relate_image_url', 'title', 'price', 'discount_price',
                  'quantity', 'stock', 'sold', 'categorie', 'description', ),

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'relate_image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Relate Images'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount Price'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity in Stock'}),
            'sold': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity in Sold'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'description': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a Category'}),

        }
