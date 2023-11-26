from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import JsonResponse


def index(request):
    return render(request, 'GenAIHealthSol\Templates\remedic\index.html')
