from django import forms
from .models import ContactUs



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['reply_sent']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control'}),
            'regarding': forms.Select(attrs={'class': 'form-control'}),
            'message_subject': forms.TextInput(
                attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }