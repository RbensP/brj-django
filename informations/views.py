from django.shortcuts import render

def index(request):
    return render(request, 'informations/informations.html')

def information(request):
    return render(request, 'informations/information.html')