from django.urls import path
from . import views

urlpatterns = [
    path('symptomsform/', views.details_view, name='details_view'),
    # Add more URL patterns as needed
]
