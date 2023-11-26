from django.urls import path
from .views import index, generate_reports

urlpatterns = [
    path('', index, name='index'),
    path('reports/', generate_reports, name='generate_reports'),
    # Add more URL patterns as needed
]