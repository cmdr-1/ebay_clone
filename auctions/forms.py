from django import forms

from .models import Listings

class ListingsForm(forms.Form):

    title = forms.CharField()
    description = forms.CharField()
    image = forms.URLField(required=False)
    initial_bid = forms.DecimalField()
    category = forms.CharField()
    listing_user = forms.CharField()


    # class Meta:
    #     model = Listings
    #     exclude = listing_user
    #     fields = [
    #         'product_listed',
    #         'product_desc',
    #         'product_img',
    #         'init_bid',
    #         'category'
    #     ]