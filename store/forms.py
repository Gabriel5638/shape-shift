from django import forms
from .models import Product
from .models import Comment
from .models import Rating 
from .models import ProductQuantity


    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating'] 

class SizeSelectionForm(forms.Form):
    size = forms.ChoiceField(choices=Product.SIZE_CHOICES)
    
    
class ProductQuantityForm(forms.ModelForm):
    class Meta:
        model = ProductQuantity
        fields = ['quantity']
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'category', 'description', 'size', 'color', 'material_composition', 'return_days', 'availability']
       