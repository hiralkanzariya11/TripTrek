from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, ProfilesUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}!')
            login(request, user)
            return redirect('profiles')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def profiles_view(request):
    if request.method == 'POST':
        form = ProfilesUpdateForm(request.POST, request.FILES, instance=request.user.profiles)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiles updated!')
            return redirect('profiles')
    else:
        form = ProfilesUpdateForm(instance=request.user.profiles)
    return render(request, 'profiles.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')
