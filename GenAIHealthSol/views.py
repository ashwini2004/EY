# app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_view(request):
    # Handle login logic here, check if the user is already logged in, etc.
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
