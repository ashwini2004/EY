from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirect to the desired page after successful login
        else:
            messages.error(request, 'Invalid username or password.')

    # Render the login page with the form
    return render(request, 'Templates\remedic\login.html')


def signup_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # You can now use these values as needed, for example, to create a new user
        # For simplicity, I'm using UserCreationForm, but you can create your custom form if needed
        form = UserCreationForm(data={'username': email, 'password1': password, 'password2': password})

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'Templates\remedic\signup.html', {'form': form})