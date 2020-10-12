from django import forms

from .models import Listings, Bid

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

    def __init__(self, *args, **kwargs):
        super(ListingsForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

# class BidForm(forms.ModelForm):

#     class Meta:
#         model = Bid
#         exclude = ('listing_user',)
#         fields = [
#             'title',
#             'description',
#             'image',
#             'initial_bid',
#             'category'
#         ]

#     def __init__(self, *args, **kwargs):
#         super(ListingsForm, self).__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#         })

