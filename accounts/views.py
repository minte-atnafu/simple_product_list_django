from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def forgot_password_view(request):
    return render(request, 'accounts/forgot_password.html')

def recovery_view(request):
    return render(request, 'accounts/recovery.html')

def set_password_view(request):
    return render(request, 'accounts/set_password.html')