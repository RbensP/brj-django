from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rendez_vous'),
    path('<int:jour_id>', views.set_rendezvous, name='jour_rendezvous'),
] 