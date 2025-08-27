from django.db import models
from django.utils import timezone

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class RecentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            created_at__gte=timezone.now() - timezone.timedelta(days=30)
        )