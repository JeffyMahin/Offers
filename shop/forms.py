from django import forms
from .models import ShopDetail


class ShopDetailForm(forms.ModelForm):
    class Meta:
        model = ShopDetail
        fields = ['name', 'location', 'contact']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shop Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shop Location'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'})
        }

        help_texts = {
            'name': None,
            'location': None,
            'contact': None,
        }
