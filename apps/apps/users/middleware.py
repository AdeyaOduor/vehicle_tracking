from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser

class PasswordExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Skip middleware for auth pages, admin, and static files
        auth_urls = [reverse('users:login'), reverse('users:logout'), 
                    reverse('users:password_change'), reverse('users:password_change_done'),
                    reverse('users:password_reset'), reverse('users:password_reset_done'),
                    reverse('users:password_reset_confirm'), reverse('users:password_reset_complete')]
        
        if (request.path.startswith('/admin/') or 
            request.path.startswith('/static/') or 
            request.path.startswith('/media/') or
            request.path in auth_urls):
            return None

        # Check if user is authenticated
        if request.user.is_authenticated:
            user = CustomUser.objects.get(pk=request.user.pk)
            
            # Check if password needs to be changed
            if user.force_password_change:
                if request.path != reverse('users:password_change'):
                    return redirect('users:password_change')
            
            # Check if password is expired
            expiry_date = user.last_password_change + timedelta(days=settings.PASSWORD_EXPIRY_DAYS)
            if timezone.now() > expiry_date:
                user.force_password_change = True
                user.save()
                if request.path != reverse('users:password_change'):
                    return redirect('users:password_change')
            
            # Show warning if password will expire soon
            warning_date = expiry_date - timedelta(days=settings.PASSWORD_WARNING_DAYS)
            if timezone.now() > warning_date and not request.session.get('password_warning_shown'):
                request.session['password_warning_shown'] = True
                from django.contrib import messages
                days_remaining = (expiry_date - timezone.now()).days
                messages.warning(request, f'Your password will expire in {days_remaining} days. Please change it soon.')

        return None