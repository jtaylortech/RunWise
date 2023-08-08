# runwise/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from .forms import RegistrationForm, LoginForm

# app/views.py

def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Has the user's password before saving
            password = make_password(form.cleaned_data['password'])
            # Create the user object with the hashed password
            user = form.save(commit=False)
            user.password = password
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle login logic (e.g., check user credentials and authenticate user)
            # After successful login, redirect to the user's profile or dashboard
            return redirect('dashboard')  # Replace 'dashboard' with the URL name for the user's profile page
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

