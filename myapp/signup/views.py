from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm

def usersignup(request):
    form = UserCreationForm(request.POST)
    return render(request, 'signup.html', {'form': form})

def userconfirm(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        return render(request, 'confirm.html', {'form': form})
    error = "入力が間違っています"
    if len(request.POST["password1"]) < 8:
        error = "パスワードが短いです"
    return render(request, 'signup.html', {'form': form,'error':error})

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

