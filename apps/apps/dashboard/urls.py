from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('national/', views.national_dashboard, name='national'),
    path('county/', views.county_dashboard, name='county'),
    path('subcounty/', views.subcounty_dashboard, name='subcounty'),
    path('driver/', views.driver_dashboard, name='driver'),
    path('access-denied/', views.access_denied, name='access_denied'),
]