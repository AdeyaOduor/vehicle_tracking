from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db.models import Count, Sum, Avg, Q
from datetime import datetime, timedelta
from apps.vehicles.models import Vehicle, Location, WorkTicket, Fueling

def is_national_admin(user):
    return user.user_type == 'national'

def is_county_admin(user):
    return user.user_type == 'county'

def is_subcounty_admin(user):
    return user.user_type == 'subcounty'

def is_driver(user):
    return user.user_type == 'driver'

@login_required
def dashboard_home(request):
    user = request.user
    
    if user.user_type == 'national':
        return national_dashboard(request)
    elif user.user_type == 'county':
        return county_dashboard(request)
    elif user.user_type == 'subcounty':
        return subcounty_dashboard(request)
    elif user.user_type == 'driver':
        return driver_dashboard(request)
    
    return render(request, 'dashboard/access_denied.html')

@login_required
@user_passes_test(is_national_admin)
def national_dashboard(request):
    vehicles = Vehicle.objects.all()
    # Add analytics and statistics logic
    context = {
        'vehicles': vehicles,
        # Add other context data
    }
    return render(request, 'dashboard/national.html', context)
