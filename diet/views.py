from django.shortcuts import render

def mediterranean_diet(request):
    return render(request, 'diet/mediterranean.html')

def paleo_diet(request):
    return render(request, 'diet/paleo.html')

def keto_diet(request):
    return render(request, 'diet/keto.html')

def carnivore_diet(request):
    return render(request, 'diet/carnivore.html')

def whole_diet(request):
    return render(request, 'diet/wholediet.html')