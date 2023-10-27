from django.shortcuts import render


def push(request):
    return render(request, 'workouts/push-pull-legs.html')

def volume(request):
    return render(request, 'workouts/german-volume.html')

def texas(request):
    return render(request, 'workouts/texas-method.html')

def juggernaut(request):
    return render(request, 'workouts/juggernaut-method.html')

def stronglifts(request):
    return render(request, 'workouts/stronglifts.html')