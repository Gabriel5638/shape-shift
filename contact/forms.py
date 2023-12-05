from django import forms
from django.core.exceptions import ValidationError
from .models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['reply_sent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'regarding': forms.Select(attrs={'class': 'form-control'}),
            'message_subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_email_address(self):
        email = self.cleaned_data.get('email_address')
        if not email:
            raise ValidationError('Please enter your email address')
        return email