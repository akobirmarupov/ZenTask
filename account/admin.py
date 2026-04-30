# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'user_permissions')}),
        ('Other info', {'fields': ('is_confirmed',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

