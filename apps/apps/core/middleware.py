from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Skip middleware for auth and static files
        if request.path.startswith('/admin/') or request.path.startswith('/static/') or request.path.startswith('/media/'):
            return None

        # Allow access to public pages
        public_urls = [reverse('core:landing'), reverse('users:login'), 
                      reverse('users:register'), reverse('users:password_reset')]
        if request.path in public_urls:
            return None

        # Check if user is authenticated
        if not request.user.is_authenticated:
            return redirect(f"{reverse('users:login')}?next={request.path}")

        # Check role-based access for dashboard
        if request.path.startswith('/dashboard/'):
            user_type = request.user.user_type
            if '/national/' in request.path and user_type != 'national':
                return redirect('dashboard:access_denied')
            elif '/county/' in request.path and user_type != 'county':
                return redirect('dashboard:access_denied')
            elif '/subcounty/' in request.path and user_type != 'subcounty':
                return redirect('dashboard:access_denied')
            elif '/driver/' in request.path and user_type != 'driver':
                return redirect('dashboard:access_denied')

        return None