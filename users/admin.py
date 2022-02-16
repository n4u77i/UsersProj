from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import User


class UserAdminConfig(UserAdmin):
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['start_date']
    list_filter = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_display = ['email', 'first_name', 'last_name', 'username', 'is_active', 'is_staff']
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'username',
                'first_name',
                'last_name',
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
            ),
        }),
        ('Personnal', {
            'fields': (
                'about',
            ),
        }),
    )
    formfield_overrides = {
        User.about: {
            'widget': Textarea(attrs={
                'rows': 10,
                'cols': 40,
            })
        }
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )
    
    
admin.site.register(User, UserAdminConfig)