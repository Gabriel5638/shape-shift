from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .models import Question, Answer
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def questionnaire(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        for question in questions:
            response = request.POST.get(f"response_{question.id}")
            rating = request.POST.get(f"rating_{question.id}")
            Answer.objects.create(
                question=question,
                user=request.user,
                response=response,
                rating=rating
            )
        # Redirect to a thank-you page after submission
        return redirect('thank_you')
    return render(
        request,
        'questionnaire/questionnaire.html',
        {'questions': questions}
    )


def thank_you_view(request):
    return render(request, 'questionnaire/thank_you.html')


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
