from django.shortcuts import get_object_or_404, render
from rendezvous.models import JourRendezVous
from datetime import date, timedelta
from .models import Information

def index(request):
    informations = Information.objects.order_by('-date_created').filter(is_published=True)
    
    today = date.today()
    end = today + timedelta(days=7)
    jours = JourRendezVous.objects.exclude(number=0).filter(day__range=[today, end])
    
    data = {
        'infos': informations,
        'jours': jours
    }

    return render(request, 'informations/informations.html', data)

def information(request, info_id):
    information = get_object_or_404(Information, pk=info_id)

    today = date.today()
    end = today + timedelta(days=7)
    jours = JourRendezVous.objects.exclude(number=0).filter(day__range=[today, end])
    
    data = {
        'info': information,
        'jours': jours
    }
    
    return render(request, 'informations/information.html', data)