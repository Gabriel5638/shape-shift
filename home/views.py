from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


