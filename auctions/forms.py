from django import forms
from .models import Listing, Bid, Comment


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description',
                  'starting_bid', 'image_url', 'category']


class BidForm(forms.ModelForm):
    class Meta:
        model = Bid  # Add this line
        fields = ['amount']
        labels = {'bid_amount': 'Bid Amount'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Add this line
        fields = ['content']
        labels = {'content': 'Comment'}
