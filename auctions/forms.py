from django import forms

from .models import Listings, Bid, Comments

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

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        exclude = ('user',)
        fields = [
            'user',
            'comment'
        ]
        
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
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

