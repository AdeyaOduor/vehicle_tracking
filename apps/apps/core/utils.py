from datetime import datetime, timedelta
from django.utils import timezone

def get_password_expiry_date():
    return timezone.now() - timedelta(days=settings.PASSWORD_EXPIRY_DAYS)

def is_password_expired(user):
    if not user.last_password_change:
        return True
    expiry_date = user.last_password_change + timedelta(days=settings.PASSWORD_EXPIRY_DAYS)
    return timezone.now() > expiry_date

def get_password_expiry_warning_date():
    return timezone.now() + timedelta(days=settings.PASSWORD_WARNING_DAYS)