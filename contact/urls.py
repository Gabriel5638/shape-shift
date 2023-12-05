from django.urls import path
from .views import submit_message, display_contact_form

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('', display_contact_form, name='display_contact_form'),
]