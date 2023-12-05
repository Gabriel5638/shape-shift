from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactUsForm


def submit_message(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
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

