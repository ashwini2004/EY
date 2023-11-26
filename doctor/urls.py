# doctor/urls.py

from django.urls import path
from .views import doctorfeedback_view, doctor_view, db_store

urlpatterns = [
    path('doctor_view/', doctor_view, name='doctor_view'),
    path('feedback/', doctorfeedback_view, name='feedback'),
    path('db_store/', db_store, name='db_store')
    # Add other URL patterns as needed
]

