from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('national/', views.national_dashboard, name='national_dashboard'),
    path('county/', views.county_dashboard, name='county_dashboard'),
    path('subcounty/', views.subcounty_dashboard, name='subcounty_dashboard'),
    path('driver/', views.driver_dashboard, name='driver_dashboard'),
]
