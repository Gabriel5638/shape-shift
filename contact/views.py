from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactUsForm


def submit_message(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database

            # Get the form data
            email = form.cleaned_data['email_address']
            subject = form.cleaned_data['message_subject']
            message = form.cleaned_data['message']

            # Compose the email message
            email_message = f"Subject: {subject}\n\nFrom: {email}\n\nMessage: {message}"

            # Send the email 
            send_mail(
                'New contact form submission',
                email_message,
                email,  # User's email as sender
                [settings.EMAIL_HOST_USER], 
                fail_silently=False,
            )

            messages.success(
                request,
                "Thanks for getting in touch! We'll get back to you ASAP!"
            )
            return redirect('success_page')  # Redirect to a success page after form submission
        else:
            messages.error(
                request,
                "There was an error when sending your message. Please try again."
            )
    # Redirect to the contact form page after submission
    return redirect('display_contact_form')


def display_contact_form(request):
    form = ContactUsForm()
    context = {'form': form}
    return render(request, 'contact/contact_form.html', context)

