from django.contrib import admin

from .models import Formulaire

class FormulaireAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'state', 'city', 'street', 'street_number', 'time_life', 'pdf','date_created',)
    list_display_links = ('id', 'state', 'city', 'street', 'street_number', 'time_life', 'pdf','date_created',)
    list_filter = ('state', 'city','date_created',)
    search_fields = ('state', 'city','date_created',)
    list_per_page = 25

admin.site.register(Formulaire, FormulaireAdmin)