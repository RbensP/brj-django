from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        print('some text')
        # messages.error(request, 'champs incorrect')
        # return redirect('register')
    else:
        return render(request, 'account/register.html')

def login(request):
    if request.method == 'POST':
        return
    else:
        return render(request, 'account/login.html')

def dashboard(request):
    return render(request, 'account/dashboard.html')

def logout(request):
    return redirect('index')
