from django import forms
from .models import Post  # , Category

#choices = Category.objects.all().values_list('name', 'name')

#choice_list = []

# for item in choices:
#    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_url', 'title', 'author',  'content', )

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control',  'value': '', 'id': 'liven', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image_url', 'title', 'author',  'content', )

        widgets = {
            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type in the Image URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'liven'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'placeholder': 'Select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type in your post here'}),

        }
