from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('informations/', include('informations.urls')),
    path('formulaire/', include('formulaire.urls')),
    path('admin/', admin.site.urls),
]