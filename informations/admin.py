from django.contrib import admin

from .models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'date_created')
    list_display_links = ('id', 'title')
    list_filter = ('date_created',)
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Information, InformationAdmin)