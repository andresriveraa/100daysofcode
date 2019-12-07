from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('post')
        else:
            return render(request, 'user/login.html', {'error': 'invalid username or password'})
    return render(request, 'user/login.html', {'post': 'users'})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
