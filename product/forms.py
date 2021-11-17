from django import forms
from .models import Product, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'title', 'price',
                  'discount_price', 'category', 'content', )

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image_url', 'title', 'price',
                  'discount_price', 'category', 'content', )

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'discount_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),

        }
