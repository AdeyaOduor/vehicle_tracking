from django.db import models
from apps.core.models import AuditModel

class DashboardSettings(AuditModel):
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class DashboardWidget(AuditModel):
    WIDGET_TYPES = [
        ('chart', 'Chart'),
        ('stat', 'Statistics'),
        ('map', 'Map'),
        ('table', 'Table'),
    ]
    
    name = models.CharField(max_length=100)
    widget_type = models.CharField(max_length=20, choices=WIDGET_TYPES)
    configuration = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name