import os
from django.shortcuts import render

def contact_form_view(request):
    EMAILJS_API_KEY = os.environ.get('EMAILJS_API_KEY')
    EMAILJS_SERVICE_ID = os.environ.get('EMAILJS_SERVICE_ID')
    EMAILJS_TEMPLATE_ID = os.environ.get('EMAILJS_TEMPLATE_ID')
    
    context = {
        'EMAILJS_API_KEY': EMAILJS_API_KEY,
        'EMAILJS_SERVICE_ID': EMAILJS_SERVICE_ID,
        'EMAILJS_TEMPLATE_ID': EMAILJS_TEMPLATE_ID,
    }
    
    return render(request, 'contact/contact.html', context)