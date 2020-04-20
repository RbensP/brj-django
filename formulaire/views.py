from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Formulaire
from .render_pdf import Render
User = get_user_model()

def index(request):
    if request.method == 'POST':
        state = request.POST['state']
        city = request.POST['city']
        street = request.POST['street']
        street_number = request.POST['street_number']
        time_number = request.POST['time_number']
        time_interval = request.POST['time_interval']
        time_life = time_number + ' ' + time_interval 
        
        user = User.objects.get(id=request.user.id)

        formulaire = Formulaire.objects.create(user=user,state=state,city=city,street=street,
        street_number=street_number,time_life=time_life)
        
        formulaire.save()

        return redirect('dashboard')
    else:
        numbers = list()
        for i in range(50):
            numbers.append(i+1)
            
        departements = [
            "Artibonite",
            "Ouest",
            "Nord",
            "Nord-Est",
            "Nord-Ouest",
            "Centre",
            "Nippes",
            'Grand-Anse',
            "Sud",
            "Sud-Est",
        ]

        data = {
            'numbers': numbers,
            'departements': departements
        }
            
        return render(request, 'formulaire/formulaire.html', data)

def render_pdf_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)

        try:
            formulaire = Formulaire.objects.get(user_id=request.user.id)
        except Formulaire.DoesNotExist:
            formulaire = None

        if formulaire is not None:
            context = {
                'user': user,
                'formulaire': formulaire
            }
            
            return Render.render('formulaire/formulaire_pdf_template.html', context)
        else:
            return redirect('formulaire')
    else:
        return redirect('login')

def render_pdf_download(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)

        try:
            formulaire = Formulaire.objects.get(user_id=request.user.id)
        except Formulaire.DoesNotExist:
            formulaire = None

        if formulaire is not None:
            context = {
                'user': user,
                'formulaire': formulaire
            }
            
            return Render.render_for_download('formulaire/formulaire_pdf_template.html', context)
        else:
            return redirect('formulaire')
    else:
        return redirect('login')