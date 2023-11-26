from django.urls import path
from . import views

urlpatterns = [
    path('symptomsform/', views.details_view, name='details_view'),
    path('feedback/', views.feedback_view, name='feedback'),
    # Add more URL patterns as needed
]
