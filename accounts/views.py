from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .forms import CustomSignupForm
from django.contrib import messages
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log the user in immediately after creation
            login(request, user)

            # Redirect to home page or another page after successful signup
            return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'form': form})

    else:
        form = CustomSignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        password = request.POST.get('password')  # Get password from the form

        # Validate email and password
        if not email or not password:
            messages.error(request, "Please provide both email and password.")
            return redirect('login')  # Redirect back to the login page

        try:
            # Find the user by email
            user = User.objects.get(email=email)
            
            # Authenticate the user using the username
            authenticated_user = authenticate(request, username=user.username, password=password)
            
            if authenticated_user is not None:
                # If authentication is successful, log the user in
                login(request, authenticated_user)
                return redirect('home')
            else:
                # If authentication fails, show an error message
                messages.error(request, "Invalid email or password.")
                return redirect('login')  # Redirect back to the login page
         
        except User.DoesNotExist:
            # If no user is found with the provided email
            messages.error(request, "No user found with this email.")
            return redirect('login')  # Redirect back to the login page
    
    else:
        # Render the login form for GET requests
        return render(request, 'accounts/login.html')


def forgot_password_view(request):
    return render(request, 'accounts/forgot_password.html')

def recovery_view(request):
    return render(request, 'accounts/recovery.html')

def set_password_view(request):
    return render(request, 'accounts/set_password.html')