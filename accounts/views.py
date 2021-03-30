from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (RegistrationForm,
                            EditProfileForm,
                            )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'AYs'
    args = {'MyName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register2.html', args)


@login_required()
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile2.html', args)


@login_required()
def edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)

        args = {'form': form}
        return render(request, 'accounts/edit2.html', args)


@login_required()
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts')
        else:
            return redirect('/accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/Change_password2.html', args)


def side_project(request):
    return render(request, 'accounts/SideProject.html')
