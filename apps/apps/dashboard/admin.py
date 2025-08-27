from django.contrib import admin
from .models import DashboardSettings

@admin.register(DashboardSettings)
class DashboardSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')
    list_editable = ('value',)