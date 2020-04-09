from django.shortcuts import get_object_or_404, render

from .models import Information

def index(request):
    informations = Information.objects.order_by('-date_created').filter(is_published=True)
    data = {
        'infos': informations
    }

    return render(request, 'informations/informations.html', data)

def information(request, info_id):
    information = get_object_or_404(Information, pk=info_id)
    data = {
        'info': information
    }
    
    return render(request, 'informations/information.html', data)