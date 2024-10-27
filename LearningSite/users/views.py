from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from .forms import UserRegistrationForm, UserLoginForm, ProfileForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            username = request.POST['username']
            password = request.POST['password']
            # Authenticate the user
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, "Успешный вход")
                return HttpResponseRedirect(reverse('main:homepage'))
    else:
        form = UserLoginForm()
        messages.error(request, "Введенные данные неверные")
    context = {
        'title': '',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, "Вы зарегестрировались")
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
        context = {
            'title': '',
            'form': form,
        }
        return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': '',
        "form": form
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    messages.success(request, "Вы вышли")
    return HttpResponseRedirect(reverse('main:homepage'))