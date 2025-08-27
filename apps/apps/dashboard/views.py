from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Sum, Avg, Q
from datetime import datetime, timedelta
from apps.vehicles.models import Vehicle, Location, WorkTicket, Fueling
from apps.users.models import CustomUser

def role_required(*roles):
    def decorator(view_func):
        decorated_view_func = user_passes_test(
            lambda u: u.is_authenticated and u.user_type in roles,
            login_url='dashboard:access_denied'
        )(view_func)
        return decorated_view_func
    return decorator

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
@role_required('national')
def national_dashboard(request):
    vehicles = Vehicle.objects.all()
    total_vehicles = vehicles.count()
    active_vehicles = vehicles.filter(status='active').count()
    maintenance_vehicles = vehicles.filter(status='maintenance').count()
    
    # County-wise statistics
    county_stats = vehicles.values('county').annotate(
        total=Count('id'),
        active=Count('id', filter=Q(status='active')),
        maintenance=Count('id', filter=Q(status='maintenance'))
    )
    
    context = {
        'vehicles': vehicles,
        'total_vehicles': total_vehicles,
        'active_vehicles': active_vehicles,
        'maintenance_vehicles': maintenance_vehicles,
        'county_stats': county_stats,
    }
    return render(request, 'dashboard/national.html', context)

@login_required
@role_required('county')
def county_dashboard(request):
    vehicles = Vehicle.objects.filter(county=request.user.county)
    total_vehicles = vehicles.count()
    active_vehicles = vehicles.filter(status='active').count()
    maintenance_vehicles = vehicles.filter(status='maintenance').count()
    
    # Subcounty-wise statistics
    subcounty_stats = vehicles.values('subcounty').annotate(
        total=Count('id'),
        active=Count('id', filter=Q(status='active')),
        maintenance=Count('id', filter=Q(status='maintenance'))
    )
    
    context = {
        'vehicles': vehicles,
        'total_vehicles': total_vehicles,
        'active_vehicles': active_vehicles,
        'maintenance_vehicles': maintenance_vehicles,
        'subcounty_stats': subcounty_stats,
    }
    return render(request, 'dashboard/county.html', context)

@login_required
@role_required('subcounty')
def subcounty_dashboard(request):
    vehicles = Vehicle.objects.filter(
        county=request.user.county, 
        subcounty=request.user.subcounty
    )
    total_vehicles = vehicles.count()
    active_vehicles = vehicles.filter(status='active').count()
    maintenance_vehicles = vehicles.filter(status='maintenance').count()
    
    context = {
        'vehicles': vehicles,
        'total_vehicles': total_vehicles,
        'active_vehicles': active_vehicles,
        'maintenance_vehicles': maintenance_vehicles,
    }
    return render(request, 'dashboard/subcounty.html', context)

@login_required
@role_required('driver')
def driver_dashboard(request):
    vehicle = get_object_or_404(Vehicle, current_driver=request.user)
    recent_tickets = WorkTicket.objects.filter(vehicle=vehicle).order_by('-created_at')[:5]
    recent_fuelings = Fueling.objects.filter(vehicle=vehicle).order_by('-date')[:5]
    
    context = {
        'vehicle': vehicle,
        'recent_tickets': recent_tickets,
        'recent_fuelings': recent_fuelings,
    }
    return render(request, 'dashboard/driver.html', context)

@login_required
def access_denied(request):
    return render(request, 'dashboard/access_denied.html')