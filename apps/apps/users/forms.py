from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'county', 'subcounty', 'phone_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type', 'county', 'subcounty', 'phone_number')

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password2(self):
        password2 = super().clean_new_password2()
        validate_password(password2, self.user)
        return password2