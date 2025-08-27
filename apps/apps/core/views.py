from django.shortcuts import render

def landing_page(request):
    context = {
        'title': 'FleetTrack - Vehicle Management System',
        'description': 'Advanced vehicle tracking and management system for efficient fleet operations'
    }
    return render(request, 'core/landing.html', context)

def about(request):
    return render(request, 'core/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'core/contact.html', {'title': 'Contact Us'})