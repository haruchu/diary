from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate,logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def usersignup(request):
    form = UserCreationForm(request.POST)
    return render(request, 'signup.html', {'form': form})


def userconfirm(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        return render(request, 'confirm.html', {'form': form})
    return render(request, 'signup.html', {'form': form})


def usercreate(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def userLogIn(request):
    context = {}
    return render(request, 'login.html',context)

def logIn(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(to='/home')
    else:
        error = "ユーザーが見つかりません"
        return render(request, 'login.html', {'error': error})

def logOut(request):
    logout(request)
    return redirect(to='/')

