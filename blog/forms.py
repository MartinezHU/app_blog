from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'sub_title',
            'content',
            'category',
            'tags'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'sub_title': 'Subtítulo',
            'content': 'Contenido',
            'category': 'Categoría',
            'tags': 'Etiquetas'
        }


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]