from django.shortcuts import render, redirect
from .models import Formulaire
from django.contrib.auth import get_user_model
User = get_user_model()

def index(request):
    if request.method == 'POST':
        state = request.POST['state']
        city = request.POST['city']
        street = request.POST['street']
        street_number = request.POST['street_number']
        time_number = request.POST['time_number']
        time_interval = request.POST['time_interval']
        time_life = time_number + time_interval 
        
        user = User.objects.get(id=request.user.id)
        formulaire = Formulaire.objects.create(user=user,state=state,city=city,street=street,
        street_number=street_number,time_life=time_life)
        
        formulaire.save()

        return redirect('dashboard')
    else:
        numbers = list()
        for i in range(50):
            numbers.append(i+1)
        
        data = {
            'numbers': numbers
        }
            
        return render(request, 'formulaire/formulaire.html', data)