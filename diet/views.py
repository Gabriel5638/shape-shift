from django.shortcuts import render
from .models import Diet

def mediterranean_diet(request):
    try:
        mediterranean = Diet.objects.get(name='Mediterranean Diet')
    except Diet.DoesNotExist:
        mediterranean = None  # Or handle the case where the diet doesn't exist

    return render(request, 'diet/mediterranean.html', {'diet': mediterranean})

def paleo_diet(request):
    paleo = Diet.objects.get(name='Paleo Diet')
    return render(request, 'diet/paleo.html', {'diet': paleo})

def keto_diet(request):
    keto = Diet.objects.get(name='Keto Diet')
    return render(request, 'diet/keto.html', {'diet': keto})

def carnivore_diet(request):
    carnivore = Diet.objects.get(name='Carnivore Diet')
    return render(request, 'diet/carnivore.html', {'diet': carnivore})

def whole_diet(request):
    whole = Diet.objects.get(name='Whole Diet')
    return render(request, 'diet/wholediet.html', {'diet': whole})