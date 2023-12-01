from django.shortcuts import render
from .models import WorkoutTracker


def workout_list(request):
    # Retrieve all WorkoutTracker instances
    workouts = WorkoutTracker.objects.all()
    
    # Pass the workouts to the template for rendering
    return render(request, 'workout_list.html', {'workouts': workouts})