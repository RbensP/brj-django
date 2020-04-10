from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import AddUserForm, UpdateUserForm

class CustomUserAdmin(BaseUserAdmin):
    form = UpdateUserForm
    add_form = AddUserForm

    list_display = ('email', 'first_name', 'last_name', 'cin', 'nif', 'is_staff')
    list_filter = ('first_name', 'last_name', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cin', 'nif')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email', 'first_name', 'last_name', 'cin', 'nif', 'password1',
                    'password2'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'cin', 'nif',)
    ordering = ('first_name', 'last_name',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)