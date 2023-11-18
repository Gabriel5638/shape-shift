from django import forms
from .models import Comment
from .models import Rating 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating'] 