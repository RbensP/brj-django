from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='formulaire'),
    path('formulaire_pdf', views.render_pdf_view, name='formulaire_pdf'),
    path('formulaire_pdf_download', views.render_pdf_download, name='formulaire_pdf_download')
] 