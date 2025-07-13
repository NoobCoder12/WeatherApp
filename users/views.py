from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def choose_action(request):
    return render(request, "users/choose.html")


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url or 'homepage')
    else:
        form = AuthenticationForm()

    next_url = request.GET.get('next', '')
    return render(request, 'users/login.html', {'form': form, 'next': next_url})


@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')


@login_required
def info(request):
    user = request.user
    return render(request, 'users/user_info.html', {'user': user})
