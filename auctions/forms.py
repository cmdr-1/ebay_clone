from django import forms

from .models import Listings

class ListingsForm(forms.ModelForm):

    class Meta:
        model = Listings
        exclude = ('listing_user',)
        fields = [
            'title',
            'description',
            'image',
            'initial_bid',
            'category'
        ]
