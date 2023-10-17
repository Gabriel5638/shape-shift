from django.shortcuts import render

def mediterranean_diet(request):
    return render(request, 'diet/mediterranean.html')
