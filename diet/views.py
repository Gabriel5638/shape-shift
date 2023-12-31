from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import MealJournalEntry
from diet.forms import MealForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
# View for creating a new meal
def meal_create(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user  # Assuming you have authentication
            meal.save()
            return redirect('meal_list')
    else:
        form = MealForm()

    return render(request, 'meal_create.html', {'form': form})


def meal_delete(request, pk):
    meal = get_object_or_404(MealJournalEntry, pk=pk)
    if request.method == 'POST':
        # Delete the meal entry
        meal.delete()
        # Return success message as JSON response
        return JsonResponse({'message': 'Meal successfully deleted'})
    # If the request method is not POST, return an error message
    return JsonResponse({'error': 'Invalid request'})


@login_required
def meal_list(request):
    meals = MealJournalEntry.objects.all()
    return render(request, 'meal_list.html', {'meals': meals})
