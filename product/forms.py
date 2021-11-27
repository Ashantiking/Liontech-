from django import forms
from .models import Product
#from category.models import Category


#choices = Category.objects.all().values_list('name','name')


#choices_list = []


# for item in choices:
# choices_list.append(item)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'image_url_1', 'image_url_2', 'title', 'price',
                  'discount_price', 'stocks', 'sold', 'slug', 'discription',)

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'image_url_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'image_url_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'discount_price'}),
            'stocks': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stocks'}),
            'sold': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sold'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            # 'category': forms.Select(choices=choices_list, attrs={'class': 'form-control', 'placeholder': 'Choose A Category'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'image_url_1', 'image_url_2', 'title', 'price',
                  'discount_price', 'stocks', 'sold', 'slug', 'discription',)

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'image_url_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'image_url_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'discount_price'}),
            'stocks': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'stocks'}),
            'sold': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'sold'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            # 'category': forms.Select(choices=choices_list, attrs={'class': 'form-control', 'placeholder': 'Choose A Category'}),
            'discription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),
        }
