from django import forms
from .models import OfferDetail


class OfferDetailForm(forms.ModelForm):
    class Meta:
        model = OfferDetail
        fields = ('name', 'product', 'image', 'offer_percentage', 'detail', 'shop_id', 'start_date', 'end_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Name'}),
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'offer_percentage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Percentage'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Offer Detail'}),
            'shop_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Shop Name'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control', 'type': 'date'}),

        }

        help_texts = {
            'name': None,
            'offer_percentage': None,
            'detail': None,
            'shop_id': None,
            'start_date': None,
            'end_date': None,
        }
