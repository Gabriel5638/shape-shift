from django import forms
from .models import Product
from .models import Comment
from .models import Rating 
from .models import ProductQuantity
from django.core.validators import MinValueValidator, MaxValueValidator

    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': '1', 'max': '10'})
        }
        validators = [
            MinValueValidator(1, message="Rating must be 1 or greater."),
            MaxValueValidator(10, message="Rating must be 10 or less.")
        ]

    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)
        self.fields['rating'].initial = 1

class SizeSelectionForm(forms.Form):
    size = forms.ChoiceField(choices=Product.SIZE_CHOICES)
    
    
class ProductQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': '1', 'oninput': 'validity.valid||(value=\'1\');'}),
        validators=[MinValueValidator(1, message="Quantity must be 1 or greater.")]
    )

    class Meta:
        model = ProductQuantity
        fields = ['quantity']
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'category', 'description', 'size', 'color', 'material_composition', 'return_days', 'availability']
       