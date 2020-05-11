from django.contrib.auth import get_user_model, authenticate, login, logout
from rendezvous.models import RendezVous, JourRendezVous
from django.shortcuts import render, redirect
from formulaire.models import Formulaire
from django.contrib import messages
from .forms import UploadFileForm
from datetime import date
User = get_user_model()
import re

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        cin_or_nif = request.POST['cin_or_nif']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if(password == password2):
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email saisi déja enregistré')
                return redirect('register')
            else:
                cleaned_first_name = re.sub(r"\s", "", first_name)
                cleaned_last_name = re.sub(r"\s", "", last_name)

                if cleaned_first_name == '' or cleaned_last_name == '':
                    messages.error(request, 'Veuilllez saisir votre nom complet')
                    return redirect('register')
                else:
                    cleaned_num = re.sub(r"\s", "", cin_or_nif)

                    if re.fullmatch(r"\d{10}", cleaned_num) == None and re.fullmatch(r"\d{3}-\d{3}-\d{3}-\d{1}", cleaned_num) == None:
                        messages.error(request, 'CIN ou NIF saisi incorrect')
                        return redirect('register')
                    else:
                        if re.fullmatch(r"\d{10}", cleaned_num):
                            if User.objects.filter(cin=cleaned_num).exists():
                                messages.error(request, 'CIN saisi déja enregistré')
                                return redirect('register')
                            else:
                                cin = cleaned_num
                                nif = ''

                        if re.fullmatch(r"\d{3}-\d{3}-\d{3}-\d{1}", cleaned_num):
                            if User.objects.filter(nif=cleaned_num).exists():
                                messages.error(request, 'NIF saisi déja enregistré')
                                return redirect('register')
                            else:
                                cin = ''
                                nif = cleaned_num

                        #There everything looks good
                        user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name,
                        password=password, cin=cin, nif=nif)

                        user.save()
                        messages.success(request, 'Enregistré! Vous pouvez vous connecter!')
                        return redirect('login')
        else:
            messages.error(request, 'Les mots de passes ne correspondent pas')
            return redirect('register')
    else:
        return render(request, 'account/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email ou Password incorrect')
            return redirect('login')

    else:
        return render(request, 'account/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        try:
            formulaire = Formulaire.objects.get(user_id=request.user.id)
        except Formulaire.DoesNotExist:
            formulaire = None
            
        try:
            rendezvous = RendezVous.objects.get(user_id=request.user.id)
        except RendezVous.DoesNotExist:
            rendezvous = None

        jour = None
        if rendezvous is not None:
            jour = JourRendezVous.objects.get(id=rendezvous.jour_id)

            if jour.day <= date.today():
                jour = None

        context = {
            'formulaire': formulaire,
            'jour_rendezvous': jour
        }

        return render(request, 'account/dashboard.html', context)
    else:
        return redirect('login')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

def edit_photo(request):
    if request.user.is_authenticated:
        return render(request, 'account/edit_photo.html')
    else:
        return redirect('login')
       
def upload_photo(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # form = UploadFileForm(request.POST, request.FILES)
            # if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.photo = request.FILES['photo']
            user.save()
                
            return redirect('dashboard')
            # else:
            #     return redirect('photo')
        else:
            return redirect('login')