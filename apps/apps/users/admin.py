from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ('username', 'email', 'user_type', 'county', 'subcounty', 'is_staff', 'is_active')
    list_filter = ('user_type', 'county', 'subcounty', 'is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_picture')}),
        ('Role Information', {'fields': ('user_type', 'county', 'subcounty')}),
        ('Password Info', {'fields': ('last_password_change', 'force_password_change')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'county', 'subcounty', 'is_staff', 'is_active')}
        ),
    )
    
    search_fields = ('username', 'email', 'county', 'subcounty')
    ordering = ('username',)