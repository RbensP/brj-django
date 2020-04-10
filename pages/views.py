from django.shortcuts import render
from django.http import HttpResponse

from informations.models import Information

def index(request):
    data = Information.objects.order_by('-date_created').filter(is_published=True)[:3]
    informations = {
        'infos': data
    }
    return render(request, 'pages/index.html', informations)

def about(request):
    return render(request, 'pages/about.html')