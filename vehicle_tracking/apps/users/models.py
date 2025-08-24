from django.contrib.auth.models import AbstractUser
from django.db import models

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
    
    def __str__(self):
        return f"{self.username} - {self.get_user_type_display()}"
