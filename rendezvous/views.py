from django.shortcuts import render, redirect, get_object_or_404
from rendezvous.models import JourRendezVous, RendezVous
from django.contrib.auth import get_user_model
from formulaire.models import Formulaire
from datetime import date, timedelta
from django.db.models import F
from datetime import date
User = get_user_model()

def index(request):
    today = date.today()
    end = today + timedelta(days=7)
    jours = JourRendezVous.objects.exclude(number=0).filter(day__range=[today, end])

    data = {
        'jours': jours
    }
    return render(request, 'rendezvous/rendezvous.html', data)

def set_rendezvous(request, jour_id):
    if request.user.is_authenticated:
        jour = get_object_or_404(JourRendezVous, pk=jour_id)
        user = User.objects.get(id=request.user.id)

        try:
            formulaire = Formulaire.objects.get(user_id=request.user.id)
        except Formulaire.DoesNotExist:
            formulaire = None

        if formulaire is not None:
            try:
                old_rdv = RendezVous.objects.get(user_id=request.user.id)
            except RendezVous.DoesNotExist:
                old_rdv = None

            if old_rdv is not None:
                old_jour = JourRendezVous.objects.get(rdv.jour_id)

                if old_jour.day >= date.today():
                    old_jour.number = F('number') + 1

                rdv.delete()

            rendezvous = RendezVous.objects.create(user=user, jour=jour)
            rendezvous.save()

            jour.number = F('number') - 1
            jour.save()

            return redirect('dashboard')

        else:
            return redirect('formulaire')
    else:
        return redirect('login')