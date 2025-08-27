from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class CustomUser(AbstractUser):
    NATIONAL = 'national'
    COUNTY = 'county'
    SUBCOUNTY = 'subcounty'
    DRIVER = 'driver'
    
    USER_TYPES = [
        (NATIONAL, 'National Admin'),
        (COUNTY, 'County Admin'),
        (SUBCOUNTY, 'Subcounty Admin'),
        (DRIVER, 'Driver'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    county = models.CharField(max_length=100, blank=True, null=True)
    subcounty = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    last_password_change = models.DateTimeField(default=timezone.now)
    force_password_change = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
    
    def save(self, *args, **kwargs):
        if self.pk and not self.force_password_change:
            # Check if password was changed
            original = CustomUser.objects.get(pk=self.pk)
            if self.password != original.password:
                self.last_password_change = timezone.now()
                self.force_password_change = False
        super().save(*args, **kwargs)