from django.conf import settings

def project_context(request):
    return {
        'PROJECT_NAME': 'FleetTrack',
        'SUPPORT_EMAIL': 'support@fleettrack.com',
        'VERSION': '1.0.0',
    }