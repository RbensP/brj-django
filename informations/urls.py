from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='informations'),
    path('<int:info_id>', views.information, name='information'),
] 