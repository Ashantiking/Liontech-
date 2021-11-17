from django import forms
from .models import Gallery  # , Category

#choices = Category.objects.all().values_list('name', 'name')

#choice_list = []

# for item in choices:
#    choice_list.append(item)


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image_url', 'title', )

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('image_url', 'title',)

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Select'}),

        }
