from django.contrib import admin
from .models import RendezVous, JourRendezVous

class JourRendezVousAdmin(admin.ModelAdmin):
    list_display = ('id','day','number',)
    list_display_links = ('id','day','number',)
    list_per_page = 25

class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','jour_id',)
    list_display_links = ('id','user_id','jour_id',)
    list_per_page = 25

admin.site.register(JourRendezVous, JourRendezVousAdmin)
admin.site.register(RendezVous, RendezVousAdmin)