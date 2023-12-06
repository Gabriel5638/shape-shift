from django.shortcuts import render

def contact_form_view(request):
    return render(request, 'contact/contact.html')