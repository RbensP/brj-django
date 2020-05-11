from informations.models import Information
from rendezvous.models import JourRendezVous
from datetime import date, timedelta
from django.shortcuts import render

def index(request):
    informations = Information.objects.order_by('-date_created').filter(is_published=True)[:3]
    
    today = date.today()
    end = today + timedelta(days=7)
    jours = JourRendezVous.objects.exclude(number=0).filter(day__range=[today, end])

    data = {
        'infos': informations,
        'jours': jours
    }

    return render(request, 'pages/index.html', data)

def about(request):
    return render(request, 'pages/about.html')