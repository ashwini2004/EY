from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.generate_reports, name='generate_reports'),
    # Add more URL patterns as needed
]