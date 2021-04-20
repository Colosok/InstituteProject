from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm


def IndexView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'mainWindow/index.html', context)


def registerPage(request):
    # if request.user.is_authenticated:
    #    return redirect('index')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/')

    context = {'form': form}
    return render(request, 'mainWindow/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


def ProjectsView(request):
    context = {}
    return render(request, 'mainWindow/register.html', context)
