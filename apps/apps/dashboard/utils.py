from datetime import datetime, timedelta
from django.db.models import Count, Sum, Avg, Q
from django.utils import timezone
from apps.vehicles.models import Vehicle, WorkTicket, Fueling

def get_vehicle_stats(queryset=None):
    if queryset is None:
        queryset = Vehicle.objects.all()
    
    return {
        'total': queryset.count(),
        'active': queryset.filter(status='active').count(),
        'maintenance': queryset.filter(status='maintenance').count(),
        'inactive': queryset.filter(status='inactive').count(),
    }

def get_maintenance_stats(days=30):
    start_date = timezone.now() - timedelta(days=days)
    tickets = WorkTicket.objects.filter(created_at__gte=start_date)
    
    return {
        'total': tickets.count(),
        'completed': tickets.filter(status='completed').count(),
        'pending': tickets.filter(status='pending').count(),
        'in_progress': tickets.filter(status='in_progress').count(),
    }

def get_fuel_consumption_stats(days=30):
    start_date = timezone.now() - timedelta(days=days)
    fuel_data = Fueling.objects.filter(date__gte=start_date).aggregate(
        total_liters=Sum('liters'),
        total_cost=Sum('cost'),
        avg_cost_per_liter=Avg('cost') / Avg('liters')
    )
    
    return fuel_data

def get_vehicle_locations(queryset=None):
    if queryset is None:
        queryset = Vehicle.objects.all()
    
    locations = []
    for vehicle in queryset:
        latest_location = vehicle.locations.first()
        if latest_location:
            locations.append({
                'vehicle': vehicle.license_plate,
                'make': vehicle.make,
                'model': vehicle.model,
                'latitude': float(latest_location.latitude),
                'longitude': float(latest_location.longitude),
                'timestamp': latest_location.timestamp,
                'status': vehicle.status
            })
    
    return locations

def generate_dashboard_data(user):
    """Generate dashboard data based on user role"""
    if user.user_type == 'national':
        vehicles = Vehicle.objects.all()
    elif user.user_type == 'county':
        vehicles = Vehicle.objects.filter(county=user.county)
    elif user.user_type == 'subcounty':
        vehicles = Vehicle.objects.filter(county=user.county, subcounty=user.subcounty)
    elif user.user_type == 'driver':
        vehicles = Vehicle.objects.filter(current_driver=user)
    else:
        vehicles = Vehicle.objects.none()
    
    return {
        'vehicle_stats': get_vehicle_stats(vehicles),
        'maintenance_stats': get_maintenance_stats(),
        'fuel_stats': get_fuel_consumption_stats(),
        'vehicle_locations': get_vehicle_locations(vehicles),
    }